
from time import time
from unittest import result
from winsound import PlaySound
import pyttsx3
import webbrowser
import smtplib
import random
import json
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
from ecapture import ecapture as ec
import sys
import pywhatkit
import requests
import time
import pyjokes
from time import sleep
import pyautogui
import random

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('FRIDAY: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning sir!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon sir!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening sir!')

greetMe()
speak("Initializing system and all projects on stand by mode")
speak("Starting all systems applications")
speak("Installing and checking all drivers")
speak("Caliberating and examining all the core processors")
speak("Checking the internet connection")
speak("Wait a moment sir")
speak("All drivers are up and running")
speak("All systems have been activated")
speak("Now I am online")
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('hmm...i dontt have an answer for that,is there something else i can help with! either Try typing the command!')
        query = str(input('Command: '))

    return query
        
def idea():
    speak("What is your idea?")
    data = myCommand().title()
    speak("You said me to remember this Idea: " + data)
    speak("i save it for further applications")
    with open("data.txt", "a", encoding="Utf-8") as r:
        print(data, file=r)
        
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
        
        
if __name__ == '__main__':
 
    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('Here you go to Youtube\n')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('Here you go to Google\n')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
            
        elif "i love you" in query:
            speak("love you too,but i am engage")
            
        elif "your boyfriend name" in query:
            speak("nope,its a secret")
            
        elif "what can you do for me" in query:
            speak("anythink you whant,just say anything")
            
        elif "stop nonsense" in query:
            speak("bla,bla,bla.....okay sir")
             
        elif "you are mad" in query or "nonsense" in query:
            speak("what you think about me,sir")
            
        elif "who are you" in query:
            speak("i am friday,also known as Female Replacement Intelligent Digital Assistant Youth is a natural-language user interface ")
            
        elif "what are you doing" in query:
            speak("i just hid a palindrone within this response,wait,did i ! i did")
        
        elif "my girlfriend" in query:
            speak("hahahaha,then you are wrong, i have more than 2x faster brain than you,so i am engaged with wifi,better luck next time")
                
        elif 'i have an idea' in query:
            idea()

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif "set alarm" in query:
            speak("Enter The Time !")
            time1 = input(":Enter The Time:")
            
            while True:
                time_ac = datetime.datetime.now()
                now = time_ac.strftime("%H:%M:%S")
                
                if now == time:
                    speak("Time to wake up sir!")
                    PlaySound('apple.mp3')
                    speak("alarm closed !")
                else:
                  break
            
        
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query or 'hi' in query:
            speak('Hello Sir')
            
        elif 'friday' in query:
            speak("sir")
            
        elif 'wake up' in query:
            speak("yes sir")
            
        elif 'okay' in query or 'ok' in query:
            speak("hmmmm")
            
        elif 'How old are you' in query:
            speak("i dont have a defined age,but my birth date is 9 september 2022")
            
        elif "who i am" in query:
            speak("If you talk then definitely you are a human.")
        
        elif "tell me joke" in query:
                speak(pyjokes.get_jokes())
            
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("you asked to locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        
        elif "who is" in query:
            query = query.replace("", "")
            quation = query
            #webbrowser.open("https://www.bing.com/search?q=/" + quation)
            try:
                pywhatkit.search(query)
                result1 = wikipedia.summary(query,3)
                speak(result1)
            except:
                speak("no suitable data available")
                
        elif "what is" in query:
            query = query.replace("", "")
            quation = query
            #webbrowser.open("https://www.bing.com/search?q=/" + quation)
            try:
                pywhatkit.search(query)
                result = wikipedia.summary(query,3)
                speak(result)
            except:
                speak("no suitable data available")
                
        elif "how" in query:
            query = query.replace("", "")
            quation = query
            #webbrowser.open("https://www.bing.com/search?q=/" + quation)
            try:
                pywhatkit.search(query)
                result = wikipedia.summary(query,3)
                speak(result)
            except:
                speak("no suitable data available")
            
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = myCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = myCommand()
            if 'yes' in snfm or 'sure' in snfm:
                speak("copy")
                file.write(" :- ")
                file.write(note)
            elif 'no need' in query:
                speak("ok sir,i save it and set a reminder for yoy")
                file.write(note)
            else:
                file.write(note)
                
        elif "show my recent notes" in query:
            speak("showing note")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
            
        elif "give me a advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)
            
        elif "take screenshot" in query:
            # win+perscr
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")
            
        elif "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
            
        elif "open task manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')
            
        elif "show all tasks" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')
                
        elif "restart the system" in query:
                speak('restarting in 5 second')
                sleep(5)
                os.system("shutdown /r /t 1")
		
        elif "shutdown the system" in query:
                speak('shutting down in 5 second')
                sleep(5)
                os.system("shutdown /s /t 1")
  
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(myCommand())
            time.sleep(a)
   
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('')
        
