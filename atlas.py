# from cmath import phase
# from email.mime import audio
# import re
# from signal import pause
# from socket import timeout

# voices= engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

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

while True:
    takecommand()
adi chu    