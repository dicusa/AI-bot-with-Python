import openai
from openai import OpenAIError, APIConnectionError, RateLimitError, APIError, AuthenticationError
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_chatgpt(prompt: str):
    """
    Sends prompt to OpenAI GPT-4 and returns (success_flag, response_text).
    On success, success_flag=True and response_text contains the answer.
    On failure, success_flag=False and response_text contains a short error message.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        answer = response['choices'][0]['message']['content'].strip()
        return True, answer

    except AuthenticationError:
        return False, "Authentication failed. Please check your API key."

    except RateLimitError:
        return False, "Rate limit exceeded. Please wait and try again later."

    except APIConnectionError:
        return False, "Failed to connect to OpenAI API. Check your network."

    except APIError:
        return False, "OpenAI API returned an error. Please try again."

    except OpenAIError:
        return False, "An error occurred with OpenAI API."

    except Exception:
        # For unexpected errors, return a generic message without the full exception string
        return False, "Sorry, I couldn't process your request due to an unexpected error."
