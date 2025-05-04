import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_chatgpt(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Sorry, I couldn't process your request. {str(e)}"
