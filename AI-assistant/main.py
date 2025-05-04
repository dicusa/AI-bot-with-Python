# main.py

from .speech import SpeechEngine
from .wakeword import wait_for_wake_word
from .commands import handle_query
from .utils import get_greeting

def main():
    speech_engine = SpeechEngine()
    reminders.start_scheduler_thread()
    speech_engine.speak(get_greeting())
    speech_engine.speak("I am Anna, your AI assistant. How may I help you?")

    while True:
        wait_for_wake_word("anna")
        speech_engine.speak("Yes, how can I help you?")
        while True:
            query = speech_engine.listen("Listening for your command...")
            if handle_query(query, speech_engine):
                break
            speech_engine.speak("Do you need anything else? Say yes to continue or no to quit.")
            if speech_engine.listen().lower() == "no":
                speech_engine.speak("Glad I could help you. Goodbye!")
                return

if __name__ == "__main__":
    main()
