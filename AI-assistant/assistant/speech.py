import pyttsx3
import speech_recognition as sr
import threading
import time

class SpeechEngine:
    def __init__(self, rate=170, voice_index=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', 1.0)
        voices = self.engine.getProperty('voices')
        if voice_index is not None and len(voices) > voice_index:
            self.engine.setProperty('voice', voices[voice_index].id)
        else:
            for v in voices:
                if "female" in v.name.lower() or "zira" in v.id.lower():
                    self.engine.setProperty('voice', v.id)
                    break
        self._speak_lock = threading.Lock()

    def speak(self, text: str):
        """Speak text in a thread-safe manner."""
        def run():
            with self._speak_lock:
                self.engine.say(text)
                self.engine.runAndWait()
        t = threading.Thread(target=run)
        t.start()
        t.join()  # Wait for speech to finish before returning

    def listen(self, prompt: str = None, retries=3, timeout=4, phrase_time_limit=6) -> str:
        recognizer = sr.Recognizer()
        for attempt in range(retries):
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
                query = recognizer.recognize_google(audio, language='en-IN')
                print(f"User said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that. Please repeat.")
                time.sleep(0.5)  # small pause before retry
            except sr.RequestError:
                self.speak("Sorry, I can't connect to the recognition service right now.")
                return ""
            except Exception as e:
                print(f"Microphone error: {e}")
                self.speak("Sorry, there was a problem with the microphone.")
                return ""
        self.speak("Sorry, I couldn't understand after several attempts.")
        return ""
