import requests
import json

# Your new OpenRouter API key
API_KEY = "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"

# Choose your model — you can replace with deepseek/deepseek-r1 if preferred
MODEL_NAME = "deepseek/deepseek-chat"

def ask_online_model(prompt):
    """Send query to an online LLM via OpenRouter."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are Kavi, a friendly and advanced AI assistant created by Koushik Creations."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        result = response.json()

        # Debug if something goes wrong
        if "choices" not in result:
            print("\n[API Debug Response]", json.dumps(result, indent=2), "\n")

        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"].strip()
        elif "error" in result:
            return f"API Error: {result['error'].get('message', 'Unknown error')}"
        else:
            return "Unexpected API response format."
    except Exception as e:
        return f"Error connecting to online model: {e}"

def basic_chat(query):
    """Always send user input to the online model."""
    if "exit" in query.lower() or "quit" in query.lower():
        return "exit"
    return ask_online_model(query)
