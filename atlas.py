
import pyttsx3                     #pip install pyttsx3
import speech_recognition as sr    #pip install SpeechRecognition
import datetime                    #pip install DateTime
import os
import sys
import wikipedia as wi             #pip install wikipedia


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

        elif 'code red' or 'take a break' or 'take rest' in  query:
             hour = int(datetime.datetime.now().hour)
             if hour>=0 and hour<=12:
                 speak("ok sir , have a nice day")
                 sys.exit()

             elif hour>=12 and hour<=18:
                 speak("ok sir , have a nice day")
                 sys.exit()   
  
             else:
                 speak("ok sir, good night")
                 speak("just let me know if you need any help")
                 sys.exit()

        elif 'who are you'  in query:
             speak("hello i'm one off the most handsome A I in the world")
             speak(", just kidding")
             speak("hello i'm jaav,  an AI assistant") 
             speak("i'm best example of artificial intelligence ")
             speak("my main work is to assist my boss")
             speak("i was made by some I T's students")

        elif 'wikipedia' in  query:
             speak("searching ', ' wikipedia' ")
             query =  query.replace("wikipedia", "")
             result = wi.summary(query,sentences = 2)
             print(result)
             speak(" according to', ' wikipedia ")
             speak(result)

TaskExecution()
