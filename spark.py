from tkinter import *
from tkinter import Menu
import tkinter as tk
import pyttsx3
import datetime
import speech_recognition as s
import pyaudio
import wikipedia
import webbrowser
import os

from bs4 import BeautifulSoup
import requests,random

eng=pyttsx3.init('sapi5')
voices=eng.getProperty('voices')
 
eng.setProperty('voice',voices)
def help():
    h="1.please press the start button to activate the assistance \n 2.Ask the assistance to search the web,open editor,paly music etc.\n3.say please quit to stop assistance\n4.say quit to close the window"
    T.insert(0.0,h)
def speak(audio):
    
    eng.say(audio)
    eng.runAndWait()
   
def greet():
    tym=int(datetime.datetime.now().hour)
    if tym>=0 and tym<=11:
        speak("good morning")
    elif tym>=12 and tym<=23:
        speak('good afternoon')
def specialgreet():
    speak("iam at your service")

def listenAndProcess():
    r=s.Recognizer()
    with s.Microphone() as source:
       
        r.pause_threshold=1
        audio=r.listen(source,timeout=20,phrase_time_limit=5)
        
    try:
       
        query=r.recognize_google(audio,language='en-in')
       
    except Exception as e:
       
        return "none"

    return query

def quitting():
   exit(0)


def main():
        
    speak('hi abdul')
    greet()
    specialgreet()
    while True:
        query=listenAndProcess().lower()
        if 'wikipedia' in query:
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=1)
           
            speak(result)
        elif 'please quit' in query:
            
            speak("signing off")
            break
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open whatsapp' in query:
            webbrowser.open('whatsappweb.com')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'play music' in query:
            music_dir='C:\\Users\\abdul salam\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(os.listdir(music_dir)))]))
        elif 'open editor' in query:
            file_dir='F:\\Notepad++\\notepad++.exe'
            os.startfile(file_dir) 
        elif 'search google for' in query:
            query=query.replace('search google for','')
            
            webbrowser.open(query)
           
        elif 'what is' in query:
            query=query.replace('what is','')
            webbrowser.open(query)
            
        elif 'who is' in query:
           
            webbrowser.open(query)
            result=wikipedia.summary(query,sentences=1)
            speak(result)
        elif 'how to' in query:
            # query=query.replace('what is','')
            webbrowser.open(query)
            result=wikipedia.summary(query,sentences=1)
            speak(result)
        elif 'quit' in query:
            quit()



window = Tk()
menu = Menu(window)
new_item = Menu(menu)

window.title("Spark Voice Assistant")
window.geometry('500x500')
root = window
B1=Button(root, text='close',command=quitting,fg='red')
B1.pack() 
B1.place(relx=0.5, rely=0.5, anchor=CENTER)
B2=Button(root, text='Start',command=main,fg='blue')
B2.pack()
B2.place(relx=0.5, rely=0.4, anchor=CENTER)
B3=Button(root, text='help',command=help,fg='green')
B3.pack()
B3.place(relx=0.5, rely=0.6, anchor=CENTER)
root=window
T=tk.Text(root, height=10, width=60)
T.place(relx=0.6, rely=0.7, anchor=CENTER)
T.pack()
root.mainloop()
window.mainloop()
tk.mainloop()
