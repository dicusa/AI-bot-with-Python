import schedule
import time
import threading
from .speech import SpeechEngine

speech_engine = SpeechEngine()

reminders = []

def add_reminder(reminder: str, delay_minutes: int):
    def job():
        speech_engine.speak(f"Reminder: {reminder}")
    schedule.every(delay_minutes).minutes.do(job)
    reminders.append((reminder, delay_minutes))

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler_thread():
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()
