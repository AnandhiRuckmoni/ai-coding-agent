# AI Coding Agent

## Overview

This project implements an AI coding agent that automatically analyses an existing Node.js repository, generates an execution plan using Google's Gemini API, modifies the relevant source files, and produces a summary of the implementation.

## Architecture

The project is divided into four main components:

- **main.py** – Orchestrates the complete workflow.
- **git_manager.py** – Clones the target GitHub repository.
- **explorer.py** – Analyses the repository structure and identifies important files.
- **planner.py** – Uses Gemini to generate a structured execution plan in JSON format.
- **modifier.py** – Uses Gemini to update the selected source files according to the execution plan.

## Workflow

The agent performs the following steps:

1. Clone the target repository.
2. Explore the repository structure.
3. Identify key project files.
4. Generate an execution plan using Gemini.
5. Modify the relevant files.
6. Generate a report summarising the planned implementation and modified files.

## Repository Exploration

The repository explorer recursively scans the project and identifies:

- Entry points
- Models
- Controllers
- Routes
- Configuration files
- `package.json`

These files are summarised and provided to the planner as context.

## Assumptions

- The target project follows a typical Node.js/Express structure.
- The Gemini API returns valid JSON for planning.
- The generated code is syntactically correct.
- The planner correctly identifies the files relevant to the requested feature.

## Trade-offs

- Repository exploration is rule-based and relies on common project conventions.
- The agent trusts the LLM output and performs minimal validation.
- Only files selected by the planner are modified.
- The current implementation does not automatically execute or verify tests after modification.

## Requirements

- Python 3.10+
- Git
- A Gemini API key

## How to Run

### 1. Clone this repository

```bash
git clone <your-repository-url>
cd ai-coding-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 4. Run the agent

```bash
python main.py
```

The agent will:

- Clone the target repository
- Analyse the project structure
- Generate an execution plan
- Modify the selected files
- Display a final execution report
