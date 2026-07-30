# AI Coding Agent

## Overview

This project implements an AI coding agent that automatically analyses an existing Node.js repository, generates an execution plan using Google's Gemini API, modifies the relevant source files, and produces a summary of the implementation.

## Architecture

The project is divided into the following components:

- **main.py** – Orchestrates the complete workflow.
- **git_manager.py** – Clones the target GitHub repository.
- **explorer.py** – Analyses the repository structure and identifies important files.
- **planner.py** – Uses the Gemini API to generate a structured execution plan in JSON format.
- **modifier.py** – Uses the Gemini API to modify the selected source files according to the execution plan.

## Architecture Flow
```text
                User Request
                      │
                      ▼
               +---------------+
               |    main.py    |
               | Orchestrator  |
               +---------------+
                      │
                      ▼
              +----------------+
              | git_manager.py |
              | Clone Repo     |
              +----------------+
                      │
                      ▼
              +----------------+
              |  explorer.py   |
              | Explore Repo   |
              +----------------+
                      │
             Repository Summary
                      │
                      ▼
              +----------------+
              |   planner.py   |
              | Gemini Planner |
              +----------------+
                      │
            JSON Execution Plan
                      │
                      ▼
              +----------------+
              |  modifier.py   |
              | Gemini Modifier|
              +----------------+
                      │
              Modified Repository
                      │
                      ▼
              Execution Summary
```
              
## Workflow

The agent performs the following steps:

1. Clone the target repository.
2. Explore the repository structure.
3. Identify key project files.
4. Generate an execution plan using Gemini.
5. Modify the relevant source files.
6. Generate a report summarising the execution plan and modified files.

## Repository Exploration

The repository explorer recursively scans the project and identifies:

- Entry points
- Models
- Controllers
- Routes
- Configuration files
- `package.json`

This information is summarised and provided to the planner as context for generating the execution plan.

## Assumptions

- The target repository follows a standard Node.js/Express project structure.
- The Gemini API returns valid JSON for the execution plan.
- The agent assumes the generated code is syntactically correct.
- The planner correctly identifies the files relevant to the requested feature.

## Trade-offs

- Repository exploration is rule-based and relies on common project conventions.
- The agent performs minimal validation of LLM-generated code.
- Only the files identified by the planner are modified.
- The current implementation does not automatically execute tests after modifying the code.

## Limitations

- The agent is designed for Node.js/Express repositories that follow common project conventions.
- Repository exploration is based on file names and directory structure rather than deep semantic analysis.
- The agent assumes the generated code is correct and does not automatically execute or validate tests.

## Requirements

- Python 3.11 or later
- Git
- A Gemini API key

## How to Run

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 3. Run the agent

```bash
python main.py
```

The agent will:

- Clone the target repository
- Analyse the repository structure
- Generate an execution plan
- Modify the selected source files
- Display a final report containing the execution plan, selected feature, files modified, and implementation steps.
