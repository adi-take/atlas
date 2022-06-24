import pyttsx3                      #pip install Pyttsx3
import speech_recognition as sr     #pip install SpeechRecognition
import datetime                     #pip install DateTime
import os
import sys
import wikipedia as wi              #pip install wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup


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
    query = query.lower()
    return query  

def TaskExecution():
    # wish()
    while True:
         query = takecommand().lower()

         if 'play music' in  query:
            music_dir = ("C:\\Users\\USER\\Music\\music.mp3")
            os.startfile(os.path.join(music_dir))
            break
          
         elif 'take rest' in query:
             hour = int(datetime.datetime.now().hour)
             if hour>=0 and hour<=12:
                 speak("ok sir , have a nice day")
                 

             elif hour>=12 and hour<=18:
                 speak("ok sir , have a nice day")
                 
                 
  
             else:
                 speak("ok sir, good night")
                 speak("just let me know if you need any help")
                    
             break 
                 
                 
         elif 'who are you'  in  query:
             speak("hello i'm one off the most handsome A I in the world")
             speak(", just kidding")
             speak("hello i'm jaav,  an AI assistant") 
             speak("i'm best example of artificial intelligence ")
             speak("my main work is to assist my boss")
             speak("i was made by some I T's students")
             
             
         elif 'time' in  query:
              strftime = datetime.datetime.now().strftime("%H %M")
              print(strftime)
              speak(F"sir,the time is{strftime}")

         elif 'wikipedia' in query:
             speak("searching ', ' wikipedia' ")
             query =  query.replace("wikipedia", "")
             result = wi.summary(query,sentences = 2)
             print(result)
             speak(" according to', ' wikipedia ")
             speak(result)
            
            
         elif 'code red'  in query:
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
                 
         elif 'open youtube' in query:
             webbrowser.open("https://www.youtube.com/")
             speak("opening youtube")
             
# for open google

         elif 'open google' in  query:
             webbrowser.open("www.google.com")
             speak("opening google")

# for open google meet

         elif 'open meet' in  query:
             webbrowser.open("https://meet.google.com/")
             speak("ok sir,opening google meet")

# for open stack overflow

         elif 'stack overflow' in  query:
             webbrowser.open("https://stackoverflow.com/")
             speak("opening stack over")

# for creators information

         elif 'creators' in  query:
             speak("jinal shah , ADITYA , A J , VARUN")
         
         elif 'jinal shah' in  query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")

         elif 'aditya' in  query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")
        
         elif 'aj' in  query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")

         elif 'varun' in  query:
            speak("he is one of my creator")
            speak("currently he is pursuing BCA from sabarmati university")

# for open whatsapp in browser
         elif 'open whatsapp' in  query:
             webbrowser.open("https://web.whatsapp.com/")
             speak("opening whatsapp web")
             
# for open visual studio code

         elif 'open code' in   query:
             os.startfile("C:\\Users\jinal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
             speak("opening visual studio code")

# for open google crome
             
         elif 'open chrome' in   query:
             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
             speak("opening google chrome")

# for open MY PC

         elif 'open my pc' in   query:
             os.startfile("C:\\Users\\USER\\Desktop\\This PC - Shortcut.lnk")
             speak("opening my pc")             

# for close crome

         elif 'close my browser' in  query:
            os.system("taskkill /im chrome.exe /f")
            # os.system("taskkill /C:\Users\jinal\Desktop\This PC - Shortcut.lnk/f")

# for open command promt

         elif 'open terminal' in  query:
             os.startfile("C:\\Users\\jinal\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
             speak("opening terminal")

# for open my computer

         elif 'open this pc' in  query:
             speak("opening this pc")
             os.startfile("C:\\Users\\jinal\Desktop\\This PC - Shortcut.lnk")

# for knowing current temprature

         elif 'temperature' in  query:
            search = "temprature in ahmedabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(F"current {search} is {temp}")

# for close music

         elif 'close music' in  query:
             os.system("taskkill /im  Music.Ui.exe /f")

# for close terminal

         elif 'close terminal' in  query:
            os.system("taskkill /im  cmd.exe /f")    
            
# open my task manager
         elif 'open my manager' in  query:
             os.startfile("C:\\Windows\\System32\\Taskmgr.exe")
             speak("opening task manager")
             
             
             
             
             
             
             
             
             
             
        
def TaskExecutionMain():
    while True:
        permission = takecommand()
        if "wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            sys.exit()
            
TaskExecutionMain()