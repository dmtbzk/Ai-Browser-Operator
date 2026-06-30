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

text                 User                   │                   ▼         ┌─────────────────┐         │     Planner     │         │  (OpenAI GPT)   │         └─────────────────┘                   │                   ▼         ┌─────────────────┐         │    Validator    │         └─────────────────┘                   │                   ▼         ┌─────────────────┐         │    Executor     │         └─────────────────┘                   │                   ▼         ┌─────────────────┐         │ Browser Tools   │         └─────────────────┘                   │                   ▼         ┌─────────────────┐         │   Playwright    │         └─────────────────┘                   │                   ▼            Browser State                   │                   ▼         ┌─────────────────┐         │   Summarizer    │         │  (OpenAI GPT)   │         └─────────────────┘                   │                   ▼                Response 

---

## Project Structure

text backend/  ├── app/ │   ├── agent/ │   │   ├── planner.py │   │   ├── validator.py │   │   ├── executor.py │   │   ├── orchestrator.py │   │   └── responder.py │   │ │   ├── browser/ │   │   ├── controller.py │   │   └── manager.py │   │ │   ├── prompts/ │   │   └── planner_prompt.py │   │ │   ├── tool_registry/ │   │   └── registry.py │   │ │   └── tools/ │       └── browser_tools.py │ ├── main.py └── requirements.txt 

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

User:

text Find React jobs in London 

Planner:

text search_browser_web 

Executor:

text Searches the web 

Observation:

text Collects browser results 

Summarizer:

text Produces a clean, user-friendly response 

---

## Tech Stack

- Python 3.14
- FastAPI
- Playwright
- OpenAI Responses API
- Uvicorn

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