# assistant/speech.py

import pyttsx3
import speech_recognition as sr

class SpeechEngine:
    def __init__(self, rate=150, voice_index=1):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        voices = self.engine.getProperty('voices')
        if len(voices) > voice_index:
            self.engine.setProperty('voice', voices[voice_index].id)

    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, prompt: str = None) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            if prompt:
                print(prompt)
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            return r.recognize_google(audio, language='en-IN').lower()
        except Exception:
            self.speak("Sorry, I didn't catch that. Please repeat.")
            return self.listen(prompt)
