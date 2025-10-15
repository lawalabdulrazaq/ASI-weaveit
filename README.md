```markdown
# 🤖 WeaveItAgent

![tag:innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)

## 🧠 Overview

**WeaveItAgent** is an **autonomous DeAI educational agent** built for the **Artificial Superintelligence (ASI) Alliance** — designed to transform developer knowledge, documentation, and tutorials into **narrated video lessons** using decentralized AI infrastructure.

It unites **Fetch.ai’s uAgents**, **SingularityNET’s MeTTa Knowledge Graph**, and the **WeaveIt AI video engine** to create a next-generation **AI educator** that perceives, reasons, and acts autonomously.

> 🎯 *Think of it as an AI-powered instructor that turns decentralized knowledge into narrated video tutorials, composable and discoverable across the ASI ecosystem.*

---

## 🧩 Features

| Capability | Description |
|-------------|--------------|
| 🤖 **Autonomous Agent** | Built with **Fetch.ai’s uAgents**, capable of understanding natural language and triggering decentralized actions. |
| 🧠 **Knowledge Reasoning** | Uses **SingularityNET’s MeTTa Knowledge Graph** to retrieve and reason over decentralized data and documentation. |
| 🎬 **Video Generation** | Integrates with **WeaveIt’s AI video engine** to convert reasoning output into narrated, visual tutorials. |
| 🔗 **Cross-Agent Collaboration** | Registered on **Agentverse**, discoverable through **ASI:One Chat Protocol** for interoperability with other agents. |
| 🌐 **Frontend Access** | Returns a clickable URL where users can **watch, download, or share** their generated tutorial videos. |

---

## 🧠 Architecture

```

+----------------------------+
|        ASI:One Chat        |
| (User sends natural query) |
+-------------+--------------+
|
v
+----------------------------+
|      WeaveItAgent (uAgent) |
|  - NLP & Intent Detection  |
|  - Calls MeTTa for context |
+-------------+--------------+
|
v
+----------------------------+
|   MeTTa Knowledge Graph    |
|  - Retrieves structured    |
|    knowledge & reasoning   |
+-------------+--------------+
|
v
+----------------------------+
|   WeaveIt AI Video Engine  |
|  - Converts text → video   |
|  - Stores to IPFS/S3       |
|  - Returns public link     |
+-------------+--------------+
|
v
+----------------------------+
|   ASI Output Response      |
| “🎥 Watch your tutorial at  |
|   weaveit.ai/watch/xyz”    |
+----------------------------+

````

---

## ⚙️ Technical Stack

| Component | Technology |
|------------|-------------|
| **Agent Framework** | [Fetch.ai uAgents](https://fetch.ai/) |
| **Reasoning Layer** | [SingularityNET MeTTa Knowledge Graph](https://singularitynet.io/) |
| **Video Engine** | [WeaveIt SDK (TypeScript)](https://weaveit.ai) |
| **Deployment** | [Agentverse MCP Server](https://agentverse.ai) |
| **Frontend Delivery** | [WeaveIt Website](https://weaveit.ai/watch/) |

---

## 🚀 How It Works (Example Flow)

**User:**  
> “Teach me how to deploy an Anchor program on Solana.”

**WeaveItAgent:**
1. Interprets the request using **Fetch.ai’s uAgent** NLP layer.
2. Retrieves contextual information using **MeTTa Knowledge Graph**.
3. Passes summarized script to **WeaveIt API** for video generation.
4. Returns a clickable URL, e.g.  
   `🎥 https://weaveit.ai/watch/solana-anchor-tutorial`

**Result:**  
User opens the link → watches a **fully narrated, generated video tutorial**.

---

## 🧩 Agent Details

| Property | Value |
|-----------|--------|
| **Agent Name** | WeaveItAgent |
| **Agent Address** | *(to be added after registration on Agentverse)* |
| **Category** | Innovation Lab |
| **Chat Protocol** | Enabled |
| **Status** | Active |

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:lawalabdulrazaq/ASI-weaveit.git
cd weaveit-agent
````

### 2️⃣ Install Dependencies

```bash
pip install uagents
# OR if using TypeScript/Node
pnpm install
```

### 3️⃣ Configure Environment

Create a `.env` file:

```
WEAVEIT_API_KEY=your_api_key_here
WEAVEIT_API_URL=https://api.weaveit.ai/generate
METTA_API_URL=https://singularitynet.io/metta
```

### 4️⃣ Run the Agent

```bash
python src/weaveit_agent.py
# or
pnpm start
```

### 5️⃣ Test on Agentverse

Register your agent on [Agentverse](https://agentverse.ai) and verify discoverability under **Innovation Lab**.

---

## 🧪 Demo Video

🎥 **Demo Link (3–5 minutes):**
[https://youtu.be/weaveit-agent-demo](https://youtu.be/weaveit-agent-demo)

The demo shows:

* Query interaction on ASI:One
* Real-time reasoning with MeTTa
* WeaveIt video generation pipeline
* Clickable output link to watch tutorial

---

## 🏆 Evaluation Alignment

| Criteria                 | How WeaveItAgent Delivers                                             |
| ------------------------ | --------------------------------------------------------------------- |
| **Functionality**        | End-to-end working agent pipeline with video generation output        |
| **ASI Tech Integration** | Uses uAgents, MeTTa, and Agentverse Chat Protocol                     |
| **Innovation**           | Introduces an autonomous *educator agent* for decentralized knowledge |
| **Real-World Impact**    | Simplifies onboarding, education, and developer training              |
| **User Experience**      | Smooth, narrative-driven demo with clear watchable outputs            |

---

## 📚 Resources

* [Fetch.ai uAgents Documentation](https://fetch.ai/)
* [SingularityNET MeTTa](https://singularitynet.io/)
* [Agentverse Platform](https://agentverse.ai/)
* [WeaveIt SDK](https://weaveit.ai)

---

## 💡 Vision

> *WeaveItAgent is redefining how humans and AI learn, teach, and share knowledge in decentralized ecosystems. One prompt. One narrated lesson. Infinite reach.*

---

## 👤 Author

**Lawal Abdulrazaq Temitope**
Founder, [WeaveItAgent](https://x.com/weaveItAgent)
Twitter: [@loganthewise](https://x.com/Loganthewise)
Email: [contact@weaveit.ai](mailto:temitopelawal925@gmail.com)

```
