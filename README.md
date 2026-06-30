# AI Browser Operator

An AI-powered browser automation framework built with Python, Playwright, FastAPI, and OpenAI.

Unlike traditional browser automation scripts, this project is designed around an Agent Architecture, where an LLM plans tasks, validates them, executes browser actions, and generates human-friendly responses.

---

## Features

- 🧠 LLM-powered Task Planner
- ✅ Plan Validation
- ⚙️ Dynamic Tool Registry
- 🌐 Browser Automation with Playwright
- 💾 Persistent Browser Sessions
- 🗂 Browser State Management
- 🔎 Web Search
- 📄 Open Web Pages
- 🔗 Extract Page Links
- 📊 Observation Collection
- ✨ AI-powered Response Summarization

---

## Architecture

```
                User
                  │
                  ▼
    ┌─────────────────┐
    │     Planner     │
    │  (OpenAI GPT)   │
    └─────────────────┘
                  │
                  ▼
    ┌─────────────────┐
    │    Validator    │
    └─────────────────┘
                  │
                  ▼
    ┌─────────────────┐
    │    Executor     │
    └─────────────────┘
                  │
                  ▼
    ┌─────────────────┐
    │  Browser Tools  │
    └─────────────────┘
                  │
                  ▼
    ┌─────────────────┐
    │   Playwright    │
    └─────────────────┘
                  │
                  ▼
           Browser State
                  │
                  ▼
    ┌─────────────────┐
    │   Summarizer    │
    │  (OpenAI GPT)   │
    └─────────────────┘
                  │
                  ▼
              Response
```

---

## Project Structure

```
backend/
├── app/
│   ├── agent/
│   │   ├── planner.py
│   │   ├── validator.py
│   │   ├── executor.py
│   │   ├── orchestrator.py
│   │   └── responder.py
│   │
│   ├── browser/
│   │   ├── controller.py
│   │   └── manager.py
│   │
│   ├── prompts/
│   │   └── planner_prompt.py
│   │
│   ├── tool_registry/
│   │   └── registry.py
│   │
│   └── tools/
│       └── browser_tools.py
│
├── main.py
└── requirements.txt

frontend/
├── src/
│   ├── components/
│   │   ├── ChatInput.jsx
│   │   ├── ChatWindow.jsx
│   │   ├── ColorModeToggle.jsx
│   │   ├── EmptyState.jsx
│   │   ├── MessageBubble.jsx
│   │   ├── Sidebar.jsx
│   │   └── TypingIndicator.jsx
│   │
│   ├── hooks/
│   │   └── useChat.js
│   │
│   ├── services/
│   │   └── api.js
│   │
│   ├── theme/
│   │   └── index.js
│   │
│   ├── App.jsx
│   └── main.jsx
│
└── package.json
```

---

## Current Capabilities

### Browser Navigation

- Open websites
- Maintain browser sessions
- Read page content
- Extract page links

### Search

- Search the web
- Store search results
- Open search results by index

### Browser State

The agent remembers:

- Current URL
- Current page title
- Latest search results

This enables follow-up requests such as:

- "Open the first result"
- "Show the current browser state"
- "Show the links on this page"

---

## Tool Registry

The project uses a centralized registry as the Single Source of Truth.

Every tool is defined once and automatically shared with:

- Planner
- Validator
- Executor

This makes adding new tools simple and keeps the architecture maintainable.

---

## Example Workflow

**User:** Find React jobs in London

**Planner:** `search_browser_web`

**Executor:** Searches the web via Google

**Observation:** Collects browser results

**Summarizer:** Produces a clean, user-friendly response with links

---

## Tech Stack

**Backend**
- Python 3.14
- FastAPI + Uvicorn
- Playwright (Chromium)
- OpenAI Responses API

**Frontend**
- React + Vite
- Chakra UI v3
- Axios

---

## Roadmap

- Multi-step task planning
- Browser reasoning loop
- Screenshot analysis (Vision)
- Form filling
- Mouse & keyboard actions
- Authentication flows
- Autonomous task execution
- Reflection and self-correction
- Browser memory improvements

---

## Philosophy

This project is not intended to be a simple browser automation script.

The goal is to build an extensible AI Browser Operator capable of planning, reasoning, executing browser tasks, and interacting with the web in an autonomous and reliable way.