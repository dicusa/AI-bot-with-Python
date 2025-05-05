# main.py

from assistant.speech import SpeechEngine
from assistant.wakeword import wait_for_wake_word
from assistant.commands import handle_query
from assistant.utils import get_greeting
from assistant.plugins import reminders

def main():
    speech_engine = SpeechEngine()
    reminders.start_scheduler_thread()
    speech_engine.speak(get_greeting())
    speech_engine.speak("I am zara, your AI assistant. How may I help you?")

    while True:
        wait_for_wake_word("zara")
        while True:
            query = speech_engine.listen("Listening for your command...")
            if handle_query(query, speech_engine):
                continue
            speech_engine.speak("Do you need anything else? Say yes to continue or no to quit.")
            if speech_engine.listen().lower() == "no":
                speech_engine.speak("Glad I could help you. Goodbye!")
                return

if __name__ == "__main__":
    main()
