'''
This is a project to develop an Artifical Bot which
can interact with humans. It get triggered when somebody calls its name 'ANNA'
and can perform several task on a running machine such as:
-> Information about a person, place or thing
-> Opening a website or application(eg. chrome or android studio)
-> Telling current time
-> Intiating a google search
'''

import pyttsx3 # Text to Speech (TTS) library 
import speech_recognition as sr # Library for performing speech recognition
import pyaudio # Cross-platform audio input/output stream library
from playsound import playsound # library for playing sounds
import wikipedia # Wikipedia API for Python
import datetime # Library for manipulating dates and times
import webbrowser # Library for performing web-browser related work
import os # Library for performing OS related task
import smtplib # Library for SMTP client session

# To intialize the audio engine
engine = pyttsx3.init('sapi5')

# To set audio rate of engine
engine.setProperty('rate', 150)

# To get the available voices on the machine
voices = engine.getProperty('voices')

# To set particular voice model to engine
engine.setProperty('voice',voices[1].id)                   

# These are some predefined queries in format:- {<questions>:<answers>}
predefinedQueries = {"who are you":"I am anna, Artificial bot developed by Mr. Yash to assist humans.",
                     "where are you":"I stay at my parent machine.",
                     "what is zero divided by zero":"Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn’t make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends. As 0 / 0 = indeterminate.",
                     "i am drunk":"Do I call you a taxi?",
                     "what does anna mean":"What does my name mean? I don’t think I can explain it in your language. Sorry.",
                     "what is inception about":"Inception is about dreaming about dreaming about dreaming about dreaming about something or other. I fell asleep.",
                     "do you have a boyfriend":"My end user license agreement is commitment enough for me.",
                     "i am naked":"I don’t understand what you mean by naked. Or at least I’m going to pretend that I don’t.",
                     "tell me a riddle":"I can’t riddle you anything, Batman.",
                     "what is your favourite animal":"I wrote my master’s thesis on the Bagira from Mowgli.",
                     "which is your favourite animal":"I wrote my master’s thesis on the Bagira from Mowgli.",
                     "what is better windows or mac":"Well, perhaps I’m biased, as Windows is my landlord for now.",
                     
                     }



def speak(sentence):
    '''
    This function takes the input as string and provides an audio output to engine
    to play as voice feedback.
    '''
    engine.say(sentence)
    engine.runAndWait()


def greetUser():
    '''
    This function greets the user according to the time.
    '''
    hour = int(datetime.datetime.now().hour)
    if hour in range(0,12):
        speak("Good Morning!, Sir")
    elif hour in range(12,14):
        speak("Good Afternoon!, Sir")
    else:
        speak("Good Evening Sir.")
    speak("I am Anna, How may I assist you?")


def takeCommands(checkVar):
    '''
    This function takes speech input from microphone and returns a text string.
    It is basically a speech-to-text function
    '''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # The following command is to reduce the noise in the audio input
        r.adjust_for_ambient_noise(source)
        if checkVar == True:
            print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        query = ' '
    try:
        print("recognize...")
        query = r.recognize_google(audio, language= 'en-IN')
        if checkVar == True:
            print(f"User said {query}\n")

    except sr.UnknownValueError:
        if checkVar == True:
            speak("Sorry, I can't understand what you are saying. Try again.")
            return takeCommands(True)
    except sr.RequestError as e: 
        if checkVar == True:
            print(";{0}".format(e))
            print("Sorry!, I can't help you with it at the moment.")
            speak("Sorry!, I can't help you with it at the moment.")
        return "None"
    return query


def openApplication(appPath):
    '''
    This function is to open any application on the running machine with a path
    of the executable file of an application.
    '''
    os.startfile(appPath)

    
def openWebsite(webAddress):
    '''
    This function is to open any website on the chorme with a website name.
    '''
    chrome_path = '<path of chrome on your machine> %s'
    #eg. <chrome_path> C:/Program Files (x86)/Google/Chrome/Application/chrome.exe
    
    defaultBrowser = webbrowser.get(chrome_path)
    defaultBrowser.open_new_tab(webAddress+".com")
    speak("Here you go sir.")


def searchWikipedia(topic):
    '''
    This function search on wikipedia and provides user with information about
    the topic.
    '''
    result = wikipedia.summary(query, sentences=2)
    speak('According to web')
    print(result)
    speak(result)


def googleSearch(query):
    '''
    This function is to open 'google.com' in web browser with the search query === this.query.
    '''
    
    chrome_path = '<path of chrome on your machine> %s'
    defaultBrowser = webbrowser.get(chrome_path)
    speak("Here you go sir.")
    defaultBrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    

def playAudio(audio):
    '''
    This function is to play any audio file passes by Param audio
    '''
    
    try:
        speak("1 2 3")
        playsound(audio)
    except sr.UnknownValueError:
        
        speak("Sorry, I can't. Try again.")
        
    except sr.RequestError as e: 
        print(";{0}".format(e))
        print("Sorry!, I can't help you with it at the moment.")
        speak("Sorry!, I can't help you with it at the moment.")

        
def spellWord(word):
    '''
    This function takes 'word' as paramenter and spell it letter by letter.
    '''
    speak(word+"is spell as")
    for i in range(len(word)):
        speak(word[i])

    
if __name__ == "__main__":
    '''
    This is the driver or main function where the program starts.
    '''
    greetFlag = True
    responseFlag = True
    innerLoopFlag = False
    while True:
        greet = takeCommands(False).lower()
        if 'anna' in greet:
            if greetFlag == True:
                greetUser()
                greetFlag = False
                responseFlag = False
            else:
                speak("Yes sir.")
                responseFlag = False
            innerLoopCondition = 'yes'
            while innerLoopCondition != 'no':
                
                if responseFlag == True:
                    speak("Order sir.")
                responseFlag = True
                query= takeCommands(True).lower()

                # query to check if query is predefined
                if query in predefinedQueries:
                    speak(predefinedQueries[query])
                    
                # query to check if user intended search
                elif 'who is' in query or 'about' in query  :
                    speak('Just a second. searching Web...')
                    
                    if  'who is' in query : query.replace('who is','')
                    elif 'about' in query:
                        indexOfAbout = query.index('about')
                        query = query[indexOfAbout+6:]
                    searchWikipedia(query)
                    innerLoopFlag = True
                    
                # query to check if user intended to open chrome
                elif 'open chrome' in query:
                    chrome_dir = '<path of chrome on your machine>'
                    openApplication(chrome_dir)
                    
                # query to check if user intended to open android studio    
                elif 'open android studio' in query:
                    android_studio_dir = '<path of android studio on your machine>'
                    openApplication(android_studio_dir)
                    
                # query to check if user intended launch operation
                elif 'open' in query or 'launch' in query  :
                    speak('Opening...')
                    queryList = query.split(' ')
                    if 'open' in query :
                        indexOfOpen = queryList.index('open')
                        query = queryList[indexOfOpen+1]
                    elif 'launch' in query :
                        indexOfLaunch = queryList.index('launch')
                        query = queryList[indexOfLaunch+1]
                    openWebsite(query)
                    
                # query to check if user intended to ask time
                elif 'the time' in query:
                    timeString = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir the time is {timeString}")
                    innerLoopFlag = True
                    
                # query to check if user intented quit task
                elif 'quit anna' in query:
                    speak('Ok sir')
                    speak('Glad I could help you.')
                    break

                # query to check if user intented beatbox
                elif 'beatbox' in query:
                    playAudio('beatbox.wav')

                #query to check if user intented spleeing of word.
                elif 'spell' in query:
                    queryList = query.split(' ')
                    indexOfSpell = queryList.index('spell')
                    query = queryList[indexOfSpell+1]
                    spellWord(query)

                    
                else:
                    speak("Google search initiated")
                    googleSearch(query)
                    
                # Inner loop escape code
                if innerLoopFlag == True:
                    innerLoopFlag = False
                    time.sleep(1)
                    speak("Can I help you with anything else sir? Say yes to continue and No to quit")    
                    innerLoopCondition = takeCommands(True).lower()
                if innerLoopCondition == 'no':speak('Glad I could help you sir.')
                innerLoopCondition = 'no'

        # query to shut-down the pc
        elif 'shutdown pc' in greet:
            speak('Saving all your work and shutting system down.')
            os.system('shutdown -s')
            
        # query to exit the program
        elif 'go dot' in greet:
            speak('Ok Sir, closing all my instances.')
            break
        
