# AI-bot-with-Python

This is a python project to develop an Artificial Bot which can interact with humans.

## Source Code

- Source code contains the explanation of each and every line of a program.
  [Jump to source code](AI-assistant.py)

## Application Description

This is a python project to develop an Artificial Bot which can interact with humans. It get triggered when somebody calls its name 'ANNA' and can perform several task on a running machine such as:

- Telling information about a person, place or thing
- Opening a website or application(eg. chrome or android studio)
- Telling current time
- Intiating a google search and many more stuff

It uses different libraries to perform tasks at several levels.

- Workflow of program:
  - It waits for audio input from microphone of a device with the help of speech-recognition library.
  - The audio input then converted into text with the help of speech-to-text (STT) recognition library.
  - The text output obtained by the STT recognition library is checked to contain a particular phrase or a word to triggr any relevant action.
  - When phrase or word is matched then the equivalent function code is called to perform the task.

## Libraries Used

1. [pyttsx3](https://pypi.org/project/pyttsx3/) :- Text to Speech (TTS) library (pip install pyttsx3)
2. [speech_recognition](https://pypi.org/project/SpeechRecognition/) :- Library for performing speech recognition (pip install SpeechRecognition)
3. [pyaudio](https://pypi.org/project/PyAudio/) :- Cross-platform audio input/output stream library (pip install PyAudio)
4. [playsound](https://pypi.org/project/playsound/) :- library for playing sounds (pip install playsound)
5. [wikipedia](https://pypi.org/project/wikipedia/) :- Wikipedia API for Python (pip install wikipedia)
6. [datetime](https://docs.python.org/3/library/datetime.html) :- Library for manipulating dates and times
7. [webbrowser](https://docs.python.org/3/library/webbrowser.html) :- Library for performing web-browser related work
8. [os](https://docs.python.org/3/library/os.html) :- Library for performing OS related task
9. [smtplib](https://docs.python.org/3/library/smtplib.html) :- Library for SMTP client session
