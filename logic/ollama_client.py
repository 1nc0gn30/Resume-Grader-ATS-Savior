import requests

def send_to_ollama(text, preset="general_review"):
    payload = {
        "model": "llama3",
        "prompt": f"""
        You are an applicant tracking system resume reviewer.

        Task: Grade the following resume based on the '{preset}' focus.
        Respond with a score out of 100 and detailed feedback. Format as:

        Score: XX
        Grade Color: Green/Yellow/Red
        ---
        Detailed Feedback:
        ...

        Resume:
        {text}
        """,
        "stream": False
    }

    try:
        res = requests.post("http://localhost:11434/api/generate", json=payload)
        return res.json().get("response", "No response from Ollama.")
    except Exception as e:
        return f"Ollama error: {str(e)}"
