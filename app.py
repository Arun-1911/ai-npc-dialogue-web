from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ollama API endpoint and your installed model
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "deepseek-r1:8b"  # Replace if your model name differs

def build_prompt(character_type: str, dialogue_style: str, profile: str, scenario: str) -> str:
    """
    Builds the prompt for Ollama including NPC type, dialogue style, profile, and scenario.
    Instructs the model to respond *only* with in-character dialogue.
    """
    return f"""
NPC PROFILE:
Type: {character_type}
Traits: {profile.strip()}

SCENARIO / PLAYER INPUT:
{scenario.strip()}

INSTRUCTION:
Respond ONLY as the NPC character described above.
Use a {dialogue_style.lower()} dialogue style.
Do NOT include internal thoughts, reflections, or meta-comments.

---

NPC:
"""

@app.route("/", methods=["GET", "POST"])
def index():
    dialogue = None
    if request.method == "POST":
        character_type = request.form.get("characterType", "").strip()
        dialogue_style = request.form.get("dialogueStyle", "").strip()
        profile = request.form.get("profile", "").strip()
        scenario = request.form.get("scenario", "").strip()

        prompt = build_prompt(character_type, dialogue_style, profile, scenario)

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

        try:
            # Increased timeout to allow for initial model load or slower responses
            response = requests.post(OLLAMA_URL, json=payload, timeout=300)
            response.raise_for_status()
            data = response.json()
            dialogue = data.get("response", "").strip()
        except requests.exceptions.RequestException as e:
            dialogue = f"Error communicating with Ollama API: {e}"
        except Exception as e:
            dialogue = f"Unexpected error: {e}"

    return render_template("index.html", dialogue=dialogue)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
