import json
import time
import logging
import uuid
import cloudscraper
from typing import Dict, Any, AsyncGenerator

from fastapi import HTTPException
from fastapi.responses import StreamingResponse, JSONResponse

from app.core.config import settings
from app.providers.base_provider import BaseProvider
from app.utils.sse_utils import create_sse_data, create_chat_completion_chunk, DONE_CHUNK

logger = logging.getLogger(__name__)

# v3.0: 服务器端会话缓存
SESSION_CACHE: Dict[str, str] = {}

class GodmodeProvider(BaseProvider):
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.base_url = "https://next-api.godmode.space"
        self.threads_url = f"{self.base_url}/threads"

    async def chat_completion(self, request_data: Dict[str, Any]) -> StreamingResponse:
        
        async def stream_generator() -> AsyncGenerator[bytes, None]:
            request_id = f"chatcmpl-{uuid.uuid4()}"
            try:
                messages = request_data.get("messages", [])
                user_prompt = messages[-1].get("content") if messages else "Hello"
                
                # v3.0: 使用 'user' 字段作为会话标识符
                session_key = request_data.get("user")
                thread_id = None

                if session_key:
                    thread_id = SESSION_CACHE.get(session_key)
                else:
                    logger.warning("请求中未找到 'user' 字段，将创建新会话。要启用上下文功能，请在请求体中提供一个唯一的 'user' 字符串。")

                is_new_thread = not thread_id
                stream_url = ""
                payload = {}

                if is_new_thread:
                    # 新会话：创建 thread，然后用空JSON触发流
                    new_thread_id = self._create_thread(user_prompt)
                    if session_key:
                        SESSION_CACHE[session_key] = new_thread_id
                        logger.info(f"为用户 '{session_key}' 创建新会话，thread_id: {new_thread_id}")
                    stream_url = f"{self.threads_url}/{new_thread_id}"
                    payload = {} # 第一次触发流用空 body
                else:
                    # 延续会话：使用已有的 thread_id 和新消息
                    logger.info(f"为用户 '{session_key}' 延续会话，thread_id: {thread_id}")
                    stream_url = f"{self.threads_url}/{thread_id}"
                    payload = {
                        "message": {
                            "id": str(uuid.uuid4()),
                            "role": "user",
                            "parts": [{"type": "text", "text": user_prompt}]
                        }
                    }

                # 统一的流式请求逻辑
                response = self.scraper.post(
                    stream_url, 
                    headers=self._prepare_headers(), 
                    json=payload, 
                    stream=True, 
                    timeout=settings.API_REQUEST_TIMEOUT
                )
                response.raise_for_status()

                # v3.0: 移除所有非标准SSE事件，只发送兼容的 chunk
                for line in response.iter_lines():
                    if line.startswith(b"data:"):
                        content = line[len(b"data:"):].strip()
                        if not content:
                            continue
                        try:
                            data = json.loads(content)
                            if data.get("type") == "text":
                                delta_content = data.get("text")
                                if delta_content:
                                    chunk = create_chat_completion_chunk(request_id, settings.DEFAULT_MODEL, delta_content)
                                    yield create_sse_data(chunk)
                        except json.JSONDecodeError:
                            logger.warning(f"无法解析 SSE 数据块: {content}")
                            continue
                
                final_chunk = create_chat_completion_chunk(request_id, settings.DEFAULT_MODEL, "", "stop")
                yield create_sse_data(final_chunk)
                yield DONE_CHUNK

            except Exception as e:
                logger.error(f"处理流时发生错误: {e}", exc_info=True)
                error_message = f"内部错误: {str(e)}"
                error_chunk = create_chat_completion_chunk(request_id, settings.DEFAULT_MODEL, error_message, "stop")
                yield create_sse_data(error_chunk)
                yield DONE_CHUNK

        return StreamingResponse(stream_generator(), media_type="text/event-stream")

    def _create_thread(self, prompt: str) -> str:
        headers = self._prepare_headers()
        # 注意：创建线程的请求体是一个包含单个消息的数组
        payload = [{"text": prompt, "type": "text"}]
        try:
            response = self.scraper.post(self.threads_url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            thread_id = data.get("id")
            if not thread_id:
                raise ValueError("'/threads' 响应中缺少 'id' 字段。")
            return thread_id
        except Exception as e:
            logger.error(f"创建新会话失败: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"无法创建新的上游聊天会话: {e}")

    def _prepare_headers(self) -> Dict[str, str]:
        return {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://godmode.space",
            "referer": "https://godmode.space/",
            "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
        }

    async def get_models(self) -> JSONResponse:
        model_data = {
            "object": "list",
            "data": [
                {"id": name, "object": "model", "created": int(time.time()), "owned_by": "lzA6"}
                for name in settings.KNOWN_MODELS
            ]
        }
        return JSONResponse(content=model_data)
