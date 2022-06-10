# from cmath import phase
# from email.mime import audio
# import re
# from signal import pause
# from socket import timeout

# voices= engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
# from typing_extensions import Self
import pyttsx3
import speech_recognition as sr    #pip install 
import datetime
import os

engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir")

    elif hour>=12 and hour<=18:
        speak("good afternoon sir")   

    else:
        speak("good evening sir")
    speak("i'm jaav, please tell me how can i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("listening......")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
        print("Recorgnizing......")
        query = r.recognize_google(audio, language='en-in')
        print(F"user said: {query}\n")
    except Exception as e:
        speak("say that again please.....")
        return "none"
    return query  

def TaskExecution():
    wish()
    while True:
        query = takecommand().lower()

        if 'play music' in query:
            music_dir = ("C:\\Users\\jinal\\Music\\music.mp3")
            os.startfile(os.path.join(music_dir))
            # sys.exit()
<<<<<<< HEAD
    jinal 
 
=======
            
TaskExecution()
<<<<<<< HEAD
=======
jinal
=======
def TaskExecution():
    wish()
    while True: 
        query = takecommand().lower()
        if 'play music' in query:
            music_dir = ("C:\\Users\\USER\\Music\\music.mp3")
            os.startfile(os.path.join(music_dir))
            # sys.exit()

>>>>>>> 07dd48e21d24dd5c8bc513cebc68920f6779c18c
