<h1 align="center">Terminal Chatbot</h1>

## Project

A general-purpose chatbot to be used by the computer terminal

## Features

- Chatbot by terminal;
- O modelo utilizado é gpt-3.5-turbo;

## Technologies/Libraries/Environment

- Windows 10 Home | 22H2
- [Visual Studio Code | 1.98.2](https://code.visualstudio.com/)
- Git | 2.43.0
- Python | 3.12.5
- Pip | 24.2

## Architecture

<p align="center">
  <img alt="Architecture" src=".github/architecture.PNG" width="100%">
</p>

## How to run

1. Go to the repository folder;
```bash
  cd general_purpose_terminal_chatbot
```

2. Go to the project folder:
```bash
  cd python/3.10.12/langchain/0.2.14
```

2. Create an account on [Platform Openai](https://platform.openai.com/):
2. Generate your key on `Plataforma Openai`:
2. Use the file `.env.example` as an example to create the file `.env` and put your key in it:

4. (optional | recommended) Run the command below to create and activate the virtual environment for the project:

Linux
```bash
  python3 -m venv venv
  source venv/bin/activate
```

Windows
```bash
  python -m venv venv
  venv/Scripts/activate
```

5. Run the command below to install the project dependencies:
```bash
  pip install -r requirements.txt
```

6. Run the command below to run the project:

Linux
```bash
  python3 main.py
```

Windows
```bash
  python main.py
```