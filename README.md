# AI Article Generator with CrewAI

A multi-agent AI article generation pipeline powered by CrewAI and Gemini 2.0 Flash.

## Features

- Research automation
- Outline generation
- Article drafting
- Editing & refinement
- Data flywheel with feedback loop

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # then set your GEMINI_API_KEY
# AI Article Generator

A multi-agent system for generating high-quality articles using the crewAI framework and Gemini AI.

## Overview

This project uses multiple AI agents working together in a crew to research, outline, write, and edit articles on any topic. It leverages Gemini's capabilities and implements a data flywheel approach to continuously improve results.

## Features

- Multi-agent collaboration with specialized roles
- Research using vector databases and web scraping
- Structured article creation pipeline
- Continuous improvement through feedback collection

## Requirements

- Python 3.10 or higher
- Gemini API key

## Installation

1. Clone this repository
2. Create a `.env` file with your Gemini API key
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To generate an article:

```bash
python -m src.AI_Article_Generator.main run
```

With custom inputs:

```bash
python -m src.AI_Article_Generator.main run --article_topic "Your Topic" --vector_db_url "your_db_url" --article_sources "url1,url2"
```

## Project Structure

```
AI_Article_Generator/
├── .env
├── pyproject.toml
├── README.md
├── requirements.txt
├── knowledge/
│   └── user_preference.txt
├── src/
│   └── AI_Article_Generator/
│       ├── __init__.py
│       ├── crew.py
│       ├── main.py
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py
└── tests/
```

## License

This project is licensed under the MIT License.