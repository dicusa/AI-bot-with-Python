# 🤖 Anna – Modular AI Voice Assistant

Anna is a modular, voice-activated AI assistant for your computer. Triggered by her name (“Anna”), she can answer questions, open apps and websites, fetch information, send emails, check the weather, read the news, set reminders, and even chat with you using GPT technology.

---

## ✨ Features

- **Wake Word Activation**: Just say “Anna” to get her attention.
- **Conversational AI**: Powered by OpenAI GPT for natural conversations.
- **Information Lookup**: Ask about people, places, or things (Wikipedia integration).
- **Web & App Automation**: Open Chrome, Android Studio, or any website by voice.
- **Google Search**: Initiate a search with your voice.
- **Time Reporting**: Ask for the current time.
- **Weather Updates**: Get current weather for any city.
- **News Headlines**: Hear the latest news on any topic.
- **Email Sending**: Send emails by dictating recipient, subject, and body.
- **Reminders**: Set voice reminders for any task.
- **Fun & Predefined Responses**: Easter eggs, jokes, and witty answers.
- **Customizable & Extensible**: Modular codebase for easy feature additions.

---

## 🏗️ Project Structure

AI-assistant/
│
├── main.py
├── config.py
├── requirements.txt
├── assistant/
│   ├── __init__.py
│   ├── speech.py
│   ├── wakeword.py
│   ├── nlu.py
│   ├── commands.py
│   ├── utils.py
│   ├── parsers.py
│   ├── web.py
│   └── plugins/
│        ├── __init__.py
│        ├── weather.py
│        ├── news.py
│        ├── emailer.py
│        └── reminders.py
└── assets/
    └── beatbox.wav


---

## 🚀 Getting Started

### 1. **Clone the repository**

>git clone https://github.com/dicusa/AI-assistant.git
>cd AI-assistant

### 2. **Install dependencies**

>pip install -r requirements.txt

### 3. **Configure API keys and paths**

- Edit `config.py` with your:
  - OpenAI API key (for GPT)
  - NewsAPI key (for news)
  - Email credentials (for sending emails)
  - Application paths (Chrome, Android Studio, etc.)

### 4. **Run the assistant**

>python main.py


---

## 🗣️ Example Voice Commands

- **“Anna, who is Ada Lovelace?”**
- **“Anna, open Chrome”**
- **“Anna, launch github”**
- **“Anna, what’s the weather in New York?”**
- **“Anna, news about technology”**
- **“Anna, send email to alice@example.com subject Meeting body Let’s meet at 3 PM”**
- **“Anna, remind me to check the oven in 10 minutes”**
- **“Anna, what is zero divided by zero?”**
- **“Anna, what time is it?”**
- **“Anna, beatbox”**
- **“Anna, spell encyclopedia”**

---

## 🧠 How It Works

- **Speech Recognition**: Listens for the wake word and user commands.
- **Text-to-Speech**: Replies in a natural voice.
- **Natural Language Understanding**: Uses GPT for open-ended queries.
- **Task Modules**: Each feature (weather, news, reminders, etc.) is a separate, pluggable module.
- **Command Parsing**: Extracts intent and entities from your speech using regex and NLU.

---

## 🛠️ Extending Anna

- **Add new skills**: Drop a new Python file in `assistant/plugins/` and register it in `commands.py`.
- **Change the wake word**: Edit `wakeword.py`.
- **Customize responses**: Edit `config.py` or add more to the NLU/GPT module.

---

## 📝 Requirements

- Python 3.8+
- See `requirements.txt` for all pip dependencies.

---

## 🔒 Security

- **Never share your API keys or email credentials publicly.**
- Use environment variables or a `.env` file for sensitive information.

---

## 🧑‍💻 Credits

- Developed by Yash Jain (original concept by Mr. Yash, modernized for 2025)
- Uses [OpenAI](https://openai.com/), [NewsAPI](https://newsapi.org/), [Wikipedia](https://pypi.org/project/wikipedia/), [python-weather](https://pypi.org/project/python-weather/), and more.

---

**Anna is your friendly, extensible, and modern AI assistant for 2025 and beyond!**  
*Feel free to fork, extend, and make her your own.*