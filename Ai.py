import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning! Kushagra')
    elif hour>=12 and hour<18:
        speak('Good Afternoon! Kushagra')
    else:
        speak('Good Evening! Kushagra')
    speak('I am Zaira, How may I help you!')

def takeCommand():
    # take input from user from microphone and return a string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for task execution based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('goggle.com')

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open geeksforgeeks' in query:
            webbrowser.open('geeksforgeeks.com')

        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            num = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, The time is {strTime}')

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)

        elif 'email to kushagra' in query:
            try:
                speak('What should I send')
                content = takeCommand()
                to  = 'yourEmail@gmail.com'
                sendEmail(to, content)
                speak('Email has been Sent!')
            except Exception as e:
                print(e)
                speak('Sorry, The email could not be sent!')


