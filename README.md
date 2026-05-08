# 🤖 MultiAgent CrewAI - AI-Powered Research & Content Generation

A sophisticated multi-agent AI system that leverages **CrewAI** and **Groq's LLMs** to autonomously research cutting-edge AI trends and generate high-quality blog posts. This project demonstrates collaborative AI agents working together like employees in a company.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup & Installation](#setup--installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [License](#license)

## 🎯 Project Overview

This project implements a **multi-agent AI orchestration system** where three specialized AI agents collaborate to:

1. **Research** the latest AI trends using web search
2. **Write** engaging blog posts based on research findings
3. **Edit** and polish content for publication

The agents work in a sequential workflow, each building upon the outputs of previous agents, simulating a real editorial team workflow.

## ✨ Features

- **🔍 Multi-Agent Collaboration**: Three specialized agents (Researcher, Writer, Editor) work together seamlessly
- **🌐 Real-Time Web Search**: Integration with DuckDuckGo for current information retrieval
- **⚡ Powered by Groq**: Fast and efficient LLM inference using Groq's Llama 3.3 70B model
- **📝 Autonomous Content Generation**: Fully automated research-to-publication pipeline
- **🎭 Role-Based Agents**: Each agent has specific goals, backstories, and capabilities
- **🔗 Task Dependencies**: Tasks intelligently chain together, with later tasks using earlier outputs
- **📊 Verbose Logging**: Detailed execution logs to track agent activities and decision-making

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│          CrewAI Orchestration Layer                 │
├─────────────────────────────────────────────────────┤
│  Agent 1: Researcher    │  Agent 2: Writer  │ Agent 3: Editor
│  (Search & Analyze)     │  (Content Gen)    │ (Refine & Polish)
└────────┬────────────────────────┬────────────────────┘
         │                        │
         ▼                        ▼
   DuckDuckGo Search         Groq LLM
   (Real-time info)          (Llama 3.3-70B)
```

### Workflow

```
Task 1: Research          Task 2: Write Blog Post      Task 3: Edit & Polish
(Researcher Agent)   →    (Writer Agent)           →   (Editor Agent)
   ↓                          ↓                            ↓
Find top 3 AI trends  →  Create 500-word post  →   Final publication-ready
with sources              using research           content in Markdown
```

## 🚀 Setup & Installation

### Prerequisites

- Python 3.9 or higher
- Groq API key (free signup at [console.groq.com](https://console.groq.com))
- Internet connection (for web search functionality)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Nuthan-hue/MultiAgent_CrewAI.git
cd MultiAgent_CrewAI
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Set your Groq API key as an environment variable (never hardcode it in the script):

```bash
# On macOS/Linux
export GROQ_API_KEY="your-groq-api-key-here"

# On Windows (PowerShell)
$env:GROQ_API_KEY="your-groq-api-key-here"

# On Windows (Command Prompt)
set GROQ_API_KEY=your-groq-api-key-here
```

Get your free Groq API key from: [https://console.groq.com/keys](https://console.groq.com/keys)

## ⚙️ Configuration

### Model Configuration

The project uses **Groq's Llama 3.3 70B model** for fast LLM inference. To change the model:

```python
# In main.py, line 11
llm = LLM(model="groq/llama-3.3-70b-versatile")

# Alternative models available:
# - groq/mixtral-8x7b-32768
# - groq/gemma-7b-it
```

### Agent Customization

Modify agent roles, goals, and backstories in the agent definitions (lines 31-57):

```python
researcher = Agent(
    role='Senior Tech Researcher',           # Change the role
    goal='Uncover groundbreaking...',        # Change the goal
    backstory='You are a curious...',        # Customize backstory
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)
```

### Task Customization

Customize tasks and their descriptions (lines 63-81):

```python
research_task = Task(
    description='Search the web to identify...',  # Task instructions
    expected_output='A detailed research...',     # Expected output format
    agent=researcher
)
```

## 📖 Usage

### Basic Execution

```bash
python main.py
```

### What to Expect

1. **Initialization**: System initializes the LLM and agents
2. **Research Phase**: Agent 1 searches for the top 3 AI trends in real-time
3. **Writing Phase**: Agent 2 writes an engaging 500-word blog post
4. **Editing Phase**: Agent 3 reviews, edits, and polishes the content
5. **Output**: Final published article appears in console

### Example Output

```
Starting the Complex Crew execution...
[Researcher Agent] Searching for latest AI trends...
[Writer Agent] Creating blog post from research...
[Editor Agent] Polishing and formatting...

######################
FINAL PUBLISHED ARTICLE
######################

[Your auto-generated blog post content here]
```

## 🧠 How It Works

### 1. **Researcher Agent**
- **Role**: Senior Tech Researcher
- **Task**: Search the web for top 3 AI trends happening right now
- **Tools**: DuckDuckGo web search
- **Output**: Detailed report with trends, descriptions, sources, and real-world impact

### 2. **Writer Agent**
- **Role**: Tech Content Writer
- **Task**: Write engaging 500-word blog post based on research
- **Dependencies**: Uses output from Researcher Agent
- **Output**: Comprehensive blog post with catchy title and engaging tone

### 3. **Editor Agent**
- **Role**: Editor-in-Chief
- **Task**: Review, refine, and polish the blog post
- **Capabilities**: Can delegate back to Writer/Researcher if needed
- **Output**: Final publication-ready content in Markdown format

### Task Dependencies

Tasks are executed sequentially with explicit context dependencies:

```python
research_task → write_task (depends on research_task)
              → edit_task (depends on write_task)
```

This ensures each agent has the necessary information from previous agents.

## 📁 Project Structure

```
MultiAgent_CrewAI/
├── main.py                 # Main application file with agent/task definitions
├── requirements.txt        # Python package dependencies
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── CONTRIBUTING.md        # Contributing guidelines
├── SETUP.md              # Detailed setup instructions
└── docs/                 # Additional documentation (optional)
    ├── ARCHITECTURE.md
    └── AGENTS.md
```

## 📦 Requirements

All dependencies are listed in `requirements.txt`:

```
crewai                      # Main CrewAI framework
langchain-groq             # Groq integration for LangChain
litellm                    # LLM API gateway
langchain-community        # Community tools and integrations
duckduckgo-search         # DuckDuckGo search API wrapper
ddgs                      # Alternative DuckDuckGo search
```

For detailed dependency information, see [requirements.txt](requirements.txt).

## 🔧 Troubleshooting

### Issue: `GROQ_API_KEY not found`

**Solution**: Ensure you've set the environment variable correctly:

```bash
export GROQ_API_KEY="your-key-here"
echo $GROQ_API_KEY  # Verify it's set
```

### Issue: Network/Search errors

**Solution**: Check your internet connection and ensure DuckDuckGo is accessible in your region.

### Issue: Slow execution

**Solution**: Groq's inference is fast, but LLM response time depends on model size and load. Llama 3.3 70B provides the best quality for this use case.

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📚 Learn More

- [CrewAI Documentation](https://docs.crewai.com/)
- [Groq API Documentation](https://console.groq.com/docs)
- [LangChain Community Tools](https://python.langchain.com/docs/integrations/tools/)
- [DuckDuckGo API](https://duckduckgo.com/duckduckgo-help-pages/)

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Nuthan-hue** - [GitHub Profile](https://github.com/Nuthan-hue)

---

**⭐ If you find this project helpful, please consider giving it a star!**

