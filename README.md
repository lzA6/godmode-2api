# 🔮 godmode-2api: 你的私人"神模式"AI 网关 🚀

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Repo](https://img.shields.io/badge/GitHub-lzA6/godmode--2api-green.svg)](https://github.com/lzA6/godmode-2api)
[![Docker Support](https://img.shields.io/badge/Docker-Ready-blue.svg?logo=docker)](https://www.docker.com/)

> "任何足够先进的技术，都与魔法无异。" —— 亚瑟·克拉克

欢迎来到 `godmode-2api` 的世界！在这里，我们相信每个人都拥有创造"魔法"的潜力。这个项目就是你手中的第一根"魔杖"，它能将 [godmode.space](https://godmode.space) 网站那强大而免费的匿名聊天能力，转化为一个你可以随心所欲控制、集成和扩展的、兼容 OpenAI 格式的 API 服务。

这不仅仅是一个工具，更是一种宣言：**我们相信，强大的 AI 能力应该更容易被每个人所触及和使用，无论你是谁，身在何处。** 我们希望通过这个项目，点燃你的创造火花，让你感受到开源精神的温暖和力量，并最终喊出那句："嘿，这太酷了，我来我也行！" 😎

---

## ✨ 项目带来了什么？(优点与核心价值)

| 特性 | 描述 (大白话) | 带来的好处 |
| :--- | :--- | :--- |
| **OpenAI 兼容** | 让 `godmode` 学会了说"OpenAI 的普通话" | 你可以无缝地将它接入任何支持 OpenAI API 的应用、软件或代码库中，比如各种桌面客户端、聊天机器人框架等，瞬间拥有"超能力"！ |
| **流式传输** | 就像看视频一样，AI 的回答一个字一个字地蹦出来，而不是等半天一下子全出来 | 体验超流畅，几乎没有等待焦虑，感觉就像在和真人实时对话 |
| **上下文对话** | 它能记住你之前说过的话！你可以和它进行有连续性的、有深度的交流 | 这让 AI 不再是"金鱼记忆"，可以处理更复杂的任务，比如帮你写代码、构思文章、角色扮演等 |
| **Docker 一键部署** | 我们把所有复杂的环境配置都打包进一个"魔法盒子"(Docker)里 | 你不需要懂任何复杂的服务器知识，只需一条命令，就能在几分钟内拥有自己的 API 服务。真正的"懒人福音"！ |
| **高性能 & 稳定** | 基于 FastAPI 和 Nginx 这对"黄金搭档"，快如闪电，稳如泰山 | 即使有很多人同时使用，服务也能保持高效响应，7x24 小时稳定运行 |
| **完全开源 & 自由** | 所有的代码都对你开放，你可以随意查看、修改、学习，甚至创造出属于你自己的版本 | 你是这个"魔法"的真正主人！没有黑箱，没有限制，只有无限的可能性和共同成长的社区 |

---

## 🤔 那么，有什么缺点呢？(保持谦逊与真实)

我们坚信，诚实是最好的品质。这个项目虽好，但并非完美：

1.  **依赖"上游"**：我们的"魔法"源泉是 `godmode.space`。如果它不稳定或改变规则，我们的项目也会受到影响。这就像我们的水电依赖于总水管一样。
2.  **会话"失忆"风险**：目前的上下文记忆是存在服务器内存里的。如果服务器重启，它会"忘记"之前的对话（但会为每个用户自动开启新对话）。
3.  **功能相对基础**：目前核心功能已经实现，但像更精细的模型参数控制、多账号管理等高级功能还有待社区共同建设。

---

## 🎯 我能在什么场景下使用它？

想象一下，你可以：

*   **打造自己的 AI 助手**：接入到你喜欢的聊天软件（如 Telegram、Discord），让它成为你的私人知识库、灵感来源或编程伙伴。
*   **增强现有应用**：为你的笔记软件、翻译工具或任何需要文本处理的应用，免费增加一个强大的 AI 大脑。
*   **学习与探索**：作为一个绝佳的学习案例，你可以通过它深入了解 API 开发、Docker、反向代理等现代化 Web 技术。
*   **进行快速原型验证**：在不花费一分钱的情况下，快速验证你关于 AI 应用的各种奇思妙想。

---

## 🛠️ 懒人一键部署教程 (Let's Go!)

别怕，整个过程比泡一杯咖啡还要简单！你只需要在你的电脑或服务器上安装好 [Git](https://git-scm.com/) 和 [Docker](https://www.docker.com/products/docker-desktop/)。

**打开你的终端（命令行工具），复制并粘贴下面这整块"咒语"，然后按下回车：**

```bash
# 1. 从 GitHub 克隆项目代码
git clone https://github.com/lzA6/godmode-2api.git

# 2. 进入项目目录
cd godmode-2api

# 3. 创建并编辑你的专属"魔法契约" (.env 文件)
# 我们先从模板复制一份
cp .env.example .env

# (可选，但强烈推荐!) 为了安全，我们来生成一个独一无二的密码
# 如果你的系统支持，可以用下面的命令生成一个，然后手动替换.env文件里的API_MASTER_KEY
# Mac/Linux:
# API_KEY=$(openssl rand -hex 16) && sed -i.bak "s/godmode-2api-default-key/$API_KEY/" .env && echo "你的新 API Key 是: $API_KEY"
# Windows (PowerShell):
# $API_KEY = -join ((0..31) | ForEach-Object { '{0:x}' -f (Get-Random -Minimum 0 -Maximum 16) }); "API_MASTER_KEY=$API_KEY" | Out-File -Encoding utf8 .env -Append; echo "你的新 API Key 已生成在 .env 文件中"
# 如果上面命令不工作，别担心，手动打开 .env 文件，把 API_MASTER_KEY=... 后面的值改成一个你自己的复杂密码就行！

# 4. 启动"魔法阵" (Docker Compose)
docker-compose up -d

# 5. 查看服务状态，确保两个服务都是 "running" 或 "up"
docker-compose ps
```

**🎉 恭喜！** 你的 `godmode-2api` 服务现在已经在 `http://localhost:8088` 上运行了！你的 API 密钥就在 `.env` 文件里。

---

## 🚀 如何使用我的 API？

现在，让我们来测试一下你的"魔法"。打开另一个终端，尝试发送一个请求。

**1. 基础对话 (开启一个新会话)**

将下面的 `YOUR_API_KEY` 替换成你在 `.env` 文件里设置的 `API_MASTER_KEY`。

```bash
curl -X POST http://localhost:8088/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
    "model": "godmode-default-model",
    "messages": [
        {
            "role": "user",
            "content": "你好，请你用苏格拉底的风格，和我探讨一下什么是'开源精神'？"
        }
    ],
    "stream": true,
    "user": "my-unique-user-id-123"
}'
```

**💡 重点解释：**
*   `stream: true`：开启流式输出，你会看到答案一个字一个字地出现。
*   `user: "my-unique-user-id-123"`：这是**实现上下文对话的关键**！把它想象成你的"用户 ID"。只要你每次请求都带上同一个 `user` 值，AI 就会记得你们之前的对话。

**2. 继续对话 (利用上下文)**

注意，我们这次只发送了新的问题，但 AI 会记得我们之前让它扮演苏格拉底！

```bash
curl -X POST http://localhost:8088/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
    "model": "godmode-default-model",
    "messages": [
        {
            "role": "user",
            "content": "那么，这种精神对于一个普通程序员来说，意味着什么？"
        }
    ],
    "stream": true,
    "user": "my-unique-user-id-123"
}'
```

看到了吗？只要 `user` 字段不变，你就可以和它一直聊下去！

---

## 🔬 技术原理大揭秘 (给好奇的你)

想知道"魔法"是如何运作的吗？这就像一场精心编排的舞台剧，每个角色各司其职。

### 🏗️ 系统架构图

```
┌─────────────────┐    HTTP Request    ┌─────────────────┐    Proxy Pass    ┌─────────────────┐
│                 │ ──────────────────> │                 │ ────────────────> │                 │
│    客户端        │                    │    Nginx        │                  │   FastAPI       │
│    (Client)     │ <────────────────── │    (反向代理)   │ <──────────────── │    (应用层)     │
│                 │   Stream Response   │                 │   SSE Stream     │                 │
└─────────────────┘                    └─────────────────┘                  └─────────┬───────┘
                                                                                      │
                                                                              ┌───────▼───────┐
                                                                              │               │
                                                                              │ Godmode       │
                                                                              │ Provider      │
                                                                              │ (核心逻辑)    │
                                                                              └───────┬───────┘
                                                                                      │
                                                                              ┌───────▼───────┐
                                                                              │               │
                                                                              │ Cloudscraper  │
                                                                              │ (反爬虫处理)  │
                                                                              └───────┬───────┘
                                                                                      │
                                                                              ┌───────▼───────┐
                                                                              │               │
                                                                              │ godmode.space │
                                                                              │ (上游API)     │
                                                                              └───────────────┘
```

**舞台剧角色介绍：**

1.  **你 (用户)**：舞台剧的导演，通过 `curl` 或其他客户端发出指令。
2.  **Nginx (优雅的接待员)**：
    *   **角色**：他是第一个接触到你请求的人，站在 `8088` 端口。
    *   **工作**：他彬彬有礼地接过你的请求，然后转交给后台真正干活的 `app` 服务。他还负责一些优化工作，比如让流式传输更顺畅 (`proxy_buffering off;`)。
    *   **文件**：`nginx.conf`、`docker-compose.yml`
3.  **FastAPI (高效的后台总管)**：
    *   **角色**：这是我们用 Python 编写的核心应用，运行在 `app` 服务里。
    *   **工作**：
        *   **验证身份 (`main.py` -> `verify_api_key`)**：检查你是否带了正确的 `API_MASTER_KEY`，就像检查门票一样。
        *   **接收指令 (`main.py` -> `/v1/chat/completions`)**：理解你的聊天请求。
        *   **分派任务**：将任务交给最懂 `godmode` 的专家——`GodmodeProvider`。
    *   **文件**：`main.py`、`app/core/config.py`
4.  **GodmodeProvider (与神沟通的翻译官)**：
    *   **角色**：这是整个项目的"灵魂"，负责与 `godmode.space` 的 API 进行真正的交互。
    *   **工作**：
        *   **记忆大师 (`SESSION_CACHE`)**：他有一个小本本（一个 Python 字典），记录着每个 `user` 对应的 `thread_id`（会话 ID）。
        *   **建立新连接 (`_create_thread`)**：如果你是新用户，他会先向 `godmode` API 发起一个请求，为你创建一个新的聊天会话，并拿到 `thread_id` 记在小本本上。
        *   **传递消息**：他将你的问题，按照 `godmode` API 的格式，发送过去。
        *   **实时翻译**：`godmode` API 以一种特殊的 SSE 格式返回信息，他会实时地将这些信息解析、重组成 OpenAI 格式的 `chunk`（数据块）。
    *   **文件**：`app/providers/godmode_provider.py`
5.  **Cloudscraper (隐身斗篷)**：
    *   **角色**：`GodmodeProvider` 的一个神奇道具。
    *   **工作**：`godmode.space` 网站被 Cloudflare（一个网络安全服务）保护着，它有时会跳出验证来阻挡机器人。`cloudscraper` 能像穿上隐身斗篷一样，智能地绕过这些验证，确保我们的请求能顺利到达。
    *   **文件**：`requirements.txt` (依赖项)、`godmode_provider.py` (使用)
6.  **SSE Utils (格式化工具箱)**：
    *   **角色**：一个专门负责打包的小助手。
    *   **工作**：将翻译官处理好的内容，严格按照 OpenAI 流式 API 的 JSON 格式打包，确保客户端能正确理解。
    *   **文件**：`app/utils/sse_utils.py`

**整个流程串起来就是：**
你 → Nginx (接待) → FastAPI (总管) → GodmodeProvider (翻译官) → [使用 Cloudscraper 斗篷] → godmode.space API → [返回 SSE] → GodmodeProvider (翻译) → [使用 SSE Utils 打包] → FastAPI → Nginx → 你

---

## 📂 项目文件结构树

```
📂 godmode-2api/
├── 📄 .env                  # 你的私人配置文件 (需要从 .env.example 复制创建)
├── 📄 .env.example          # 配置文件的模板
├── 📄 .gitignore            # 告诉 Git 忽略哪些文件 (比如 .env)
├── 📄 Dockerfile            # 构建 Python 应用的"蓝图"
├── 📄 docker-compose.yml    # "一键启动"的魔法编排文件
├── 📄 main.py               # FastAPI 应用的入口，负责路由和安全
├── 📄 nginx.conf            # Nginx 反向代理的配置文件
├── 📄 requirements.txt      # Python 项目的依赖清单
└── 📂 app/
    ├── 📂 core/
    │   ├── 📄 __init__.py
    │   └── 📄 config.py       # 从 .env 读取配置并加载到应用中
    ├── 📂 providers/
    │   ├── 📄 __init__.py
    │   ├── 📄 base_provider.py # 定义了所有 Provider 应该遵守的"契约" (抽象基类)
    │   └── 📄 godmode_provider.py # 项目的核心逻辑，与 godmode.space 交互
    └── 📂 utils/
        └── 📄 sse_utils.py    # 创建 OpenAI 兼容的 SSE 数据块的工具函数
```

---

## 🌟 各方面能力评级 & 深度解析

| 方面 | 评级 | 解释 (专业术语 + 大白话) |
| :--- | :--- | :--- |
| **代码质量** | ★★★★☆ | **Pro**：代码遵循了 FastAPI 的最佳实践，使用了依赖注入 (`Depends`) 和配置管理 (`pydantic-settings`)，结构清晰。<br>**大白话**：代码写得像一本分类清晰的书，找东西很方便，也容易读懂。 |
| **技术先进性** | ★★★★☆ | **Pro**：使用了 `FastAPI` (ASGI)、`async/await`、`Docker` 等现代化技术栈，性能和开发效率都很高。<br>**大白话**：我们用的都是时下流行且强大的工具，不是"老古董"。 |
| **易用性 (UX)** | ★★★★★ | **Pro**：提供了与 OpenAI 完全一致的 API 接口和一键部署脚本，用户学习成本极低。<br>**大白话**：你几乎不用学新东西，会用 OpenAI 就会用它，安装也超级简单。 |
| **运行性能** | ★★★★☆ | **Pro**：`Uvicorn` + `FastAPI` 的组合性能卓越，Nginx 进一步优化了静态资源和并发。瓶颈主要在上游 API 的响应速度。<br>**大白话**：我们的服务本身跑得飞快，最终速度取决于 `godmode.space` 那边给答案的速度。 |
| **可扩展性** | ★★★☆☆ | **Pro**：`BaseProvider` 的设计为未来接入更多类似的服务（如其他免费 AI 网站）打下了良好基础。<br>**Con**：当前会话管理机制简单，不利于水平扩展。<br>**大白话**：想让它支持更多免费 AI 很容易，但想让 100 台机器同时跑这个服务且共享记忆，还需要一些改造。 |
| **稳定性** | ★★★☆☆ | **Pro**：Docker 和 `unless-stopped` 策略保证了服务的自愈能力。<br>**Con**：强依赖外部 API，且没有复杂的重试和熔断机制。<br>**大白话**：我们的服务自己轻易不会挂，但如果 `godmode.space` 挂了，我们也只能跟着"休息"一下。 |

---

## 🗺️ 未来蓝图 & 如何贡献 (一起来创造！)

这个项目只是一个起点，真正的"神模式"需要我们共同开启。

**✅ 现阶段已完成：**

*   核心的 OpenAI 格式转换代理功能
*   支持流式响应和上下文对话
*   通过 Docker 实现简单、可靠的部署

**⏳ 不足与待实现点：**

1.  **持久化会话 (`Persistence`)**：当前的会话 ID 存储在内存中，服务重启即丢失
2.  **多节点支持 (`Scalability`)**：如果要部署多个实例，需要一个共享的会话存储（如 Redis）
3.  **更强的容错性 (`Resilience`)**：增加对上游 API 错误的重试、超时和熔断机制
4.  **模型参数透传 (`Flexibility`)**：允许用户传递更多参数（如 temperature）给上游
5.  **多 Provider 支持 (`Extensibility`)**：增加对其他类似平台的 Provider 实现
6.  **一个简单的 Web UI (`Usability`)**：提供一个简单的网页界面，方便直接进行聊天和管理 API Key

**🚀 技术路径与扩展建议 (给未来的开发者)：**

*   **实现持久化会话**：
    *   **路径**：引入 `redis-py` 库。在 `godmode_provider.py` 中，将 `SESSION_CACHE` 从一个字典 `Dict` 改为一个 Redis 客户端实例。将 `SESSION_CACHE[session_key] = new_thread_id` 的操作改为 `redis_client.set(session_key, new_thread_id, ex=3600)` (例如，设置 1 小时过期)。
    *   **难度**：★★☆☆☆
    *   **价值**：★★★★★ (极大提升用户体验)

*   **增加 Provider 抽象**：
    *   **路径**：在 `app/providers/` 目录下创建 `claude_provider.py` 或 `llama_provider.py`。在 `main.py` 中，根据用户请求的 `model` 字段（例如 `"model": "godmode-claude"`），动态选择加载哪个 Provider。这可能需要一个 Provider 注册和发现机制。
    *   **难度**：★★★☆☆
    *   **价值**：★★★★★ (让项目成为一个真正的"AI 网关")

*   **增强安全性**：
    *   **路径**：允许在 `.env` 中配置多个 API Key，或者使用数据库来管理用户和他们的 Key。可以研究一下 FastAPI 的安全扩展库。
    *   **难度**：★★★☆☆
    *   **价值**：★★★★☆ (对于公开部署非常重要)

**我们热烈欢迎任何形式的贡献！** 无论是一个错字修正、一个功能建议，还是一个完整的 Pull Request，都是对社区的巨大支持。你可以：

1.  在 [Issues](https://github.com/lzA6/godmode-2api/issues) 中提出你的想法或遇到的问题。
2.  Fork 本项目，在自己的分支上进行修改，然后提交 Pull Request。

> 记住，开源的真正力量，不在于某一个天才的灵光一闪，而在于无数普通人愿意伸出援手，共同将一件"还不错"的事情，做得"无可挑剔"。

---

## 📜 开源协议 (License)

本项目采用 **Apache 2.0** 开源协议。

简单来说，这意味着：

*   **你可以自由地**：商用、修改、分发和私用。
*   **你需要**：在你的衍生作品中包含原始的版权和协议声明。
*   **你不需要**：开源你的修改。

这给予了你最大的自由，我们只希望这份小小的火种，能在你的手中燃烧得更旺。

---

**最后，感谢你的阅读。愿你在探索 AI 的旅途中，充满乐趣与发现！💖**

---

*文档版本：v1.0 | 最后更新：2024年*

**小提示**：如果你在使用过程中遇到任何问题，或者有好的想法和建议，欢迎随时在 GitHub 仓库中提出。我们相信，最好的产品来自于社区的共同努力！
