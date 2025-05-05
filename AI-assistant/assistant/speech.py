import pyttsx3
import speech_recognition as sr

class SpeechEngine:
    def __init__(self, rate=170, voice_index=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', 1.0)
        voices = self.engine.getProperty('voices')
        # Try to pick a female English voice if available
        if voice_index is not None and len(voices) > voice_index:
            self.engine.setProperty('voice', voices[voice_index].id)
        else:
            # Try to auto-select a female/en voice
            for i, v in enumerate(voices):
                if "female" in v.name.lower() or "zira" in v.id.lower():
                    self.engine.setProperty('voice', v.id)
                    break

    def speak(self, text: str):
        """Speaks the given text aloud."""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, prompt: str = None, timeout=4, phrase_time_limit=6) -> str:
        """Listens for a voice command and returns it as text."""
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                recognizer.energy_threshold = 3000
                recognizer.dynamic_energy_threshold = False
                recognizer.pause_threshold = 0.7
                if prompt:
                    print(prompt)
                    self.speak(prompt)
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            try:
                query = recognizer.recognize_google(audio, language='en-IN')
                print(f"User said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that. Please repeat.")
                return self.listen(prompt)
            except sr.RequestError:
                self.speak("Sorry, I can't connect to the recognition service right now.")
                return ""
        except Exception as e:
            print(f"Microphone error: {e}")
            self.speak("Sorry, there was a problem with the microphone.")
            return ""
