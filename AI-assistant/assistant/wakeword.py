# assistant/wakeword.py

import speech_recognition as sr

def wait_for_wake_word(wake_word="anna"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word...")
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='en-IN').lower()
                if wake_word in text:
                    print("Wake word detected!")
                    return
            except Exception:
                continue
