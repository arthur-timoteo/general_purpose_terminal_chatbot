## Technologies/Libraries/Environment

- Windows 10 Home | 22H2
- [Visual Studio Code | 1.98.2](https://code.visualstudio.com/)
- Git | 2.43.0
- Python | 3.12.5
- Pip | 24.2

## How to run

1. Go to the repository folder;
```bash
  cd general_purpose_terminal_chatbot
```

2. Go to the project folder:
```bash
  cd python/3.10.12/langchain/0.2.14
```

3. Create an account on [Platform Openai](https://platform.openai.com/):
4. Generate your key on `Plataforma Openai`:
5. Use the file `.env.example` as an example to create the file `.env` and put your key in it:

6. (optional | recommended) Run the command below to create and activate the virtual environment for the project:

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

7. Run the command below to install the project dependencies:
```bash
  pip install -r requirements.txt
```

8. Run the command below to run the project:

Linux
```bash
  python3 main.py
```

Windows
```bash
  python main.py
```