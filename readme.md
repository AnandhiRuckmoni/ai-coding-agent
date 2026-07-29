# AI Coding Agent

## Overview

This project implements an AI coding agent that automatically explores an existing repository, creates an execution plan using an LLM, modifies the relevant source files, and generates a summary of the changes.

## Architecture

- main.py – Entry point
- git_manager.py – Clones the repository
- explorer.py – Explores the repository structure
- planner.py – Generates an execution plan using Gemini
- modifier.py – Modifies source files using Gemini

## Agent Workflow

1. Clone the repository.
2. Explore the repository structure.
3. Identify important files.
4. Generate an execution plan.
5. Modify the relevant files.
6. Generate a report.

## Repository Exploration

The explorer recursively scans the repository and identifies:
- Entry points
- Models
- Controllers
- Routes
- Configuration files
- package.json

## Assumptions

- The repository follows a standard Node.js Express structure.
- Gemini returns valid code.
- The repository compiles after modifications.

## Trade-offs

- Repository exploration is rule-based rather than semantic.
- Validation is limited to ensuring the project starts successfully.
- Only files identified by the planner are modified.

## How to Run

1. Create a `.env` file containing:

GEMINI_API_KEY=YOUR_API_KEY

2. Install Python dependencies

3. Run:

python main.py