# AI NPC Dialogue Generator

An interactive Flask-based web app that generates **immersive NPC (Non-Playable Character) dialogue** using the locally running **Ollama API** with the `deepseek-r1:8b` language model.  
The app allows you to select NPC character types, dialogue styles, and scenarios, then generates in-character dialogue in real-time with smooth animations.

---

## 📌 Features

### Backend (Flask)
- Python Flask server (`app.py`) serving the frontend and handling API requests.
- Communicates with a **locally running Ollama server** hosting the `deepseek-r1:8b` model.
- Builds **customized prompts** combining:
  - NPC character type (Pirate, Wizard, Knight, etc.)
  - Dialogue style (Friendly, Sarcastic, Mysterious, etc.)
  - Profile traits and scenario.
- Handles request **timeouts** and **error cases** gracefully.

### Frontend (HTML + CSS + JS)
- **Dark theme** responsive UI (`templates/index.html`).
- Dropdown menus for character type & dialogue style.
- Animated input fields with cycling placeholder text.
- **Loading overlay** with a spinner during AI generation.
- **Typewriter animation** for displaying AI responses.
- Preserves form input after submission.

### Prompt Engineering
- Ensures AI **only produces immersive in-character dialogue** (no internal thoughts or technical notes).
- Injects context like character type, traits, scenario, and style into the prompt for tailored responses.

---

## 🛠 Prerequisites

Before running the project, make sure you have:

1. **Python 3.8+** installed  
   [Download here](https://www.python.org/downloads/)

2. **VS Code** installed  
   [Download here](https://code.visualstudio.com/)

3. **Ollama** installed and running locally  
   [Download here](https://ollama.com/download)

4. **deepseek-r1:8b** model pulled into Ollama  
   ```bash
   ollama pull deepseek-r1:8b

## RU INSTRUCTION
 numbered, step-by-step instructions you can follow in VS Code:

Clone or open the project: git clone https://github.com/your-username/your-repo.git && cd your-repo (or just open the project folder in VS Code if you already have it).

Open a VS Code terminal: Terminal → New Terminal.

Create a virtual environment: python -m venv venv.

Activate the virtual environment:

PowerShell (Windows): .\venv\Scripts\Activate

Command Prompt (Windows): venv\Scripts\activate.bat

macOS / Linux: source venv/bin/activate

Install dependencies: pip install -r requirements.txt.

Open a second terminal (must be separate) and prepare Ollama: (only once) ollama pull deepseek-r1:8b.

Start Ollama in that second terminal and keep it running: ollama run deepseek-r1:8b (leave this terminal open).

Back in your project terminal (venv active) start the Flask app: python app.py (or flask run if configured).

Open the app in your browser: go to http://127.0.0.1:5000.

If something fails: confirm Python ≥3.8, the venv is activated, Ollama is running (only one instance) and the model is loaded, and that Ollama’s default port (11434) isn’t blocked. To check the Ollama port:

Windows: netstat -ano | findstr 11434

mac/Linux: lsof -i :11434

If responses are slow or time out: increase the request timeout in app.py (the place where the HTTP request to Ollama is made) and restart the Flask app.

That’s it — follow 1→9 to run the app; use 10–11 for quick troubleshooting
