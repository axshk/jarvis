import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

Dict = {
    'personal' : 'aashutosh.ucholiya1@gmail.com',
    'educational' : 'b20174@students.iitmandi.ac.in'
}



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  

    else:
        speak("Good Evening!")  

    speak("Hello, I am Jarvis. An AI designed to make your life easy. How may I help you ?")      

def takeCommand():
    #It accesses microphone and take input from the user and returns a string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open linkedIn' in query:
                    webbrowser.open("linkedin.com")

        elif 'open github' in query:
                    webbrowser.open("github.com")

        elif 'open spotify' in query:
                    webbrowser.open("spotify.com")


        elif 'play music' in query:
            music_dir = 'JARVIS/Songs'
            songs = os.listdir(music_dir)
            rand=random.randint(0,len(songs))   
            os.startfile(os.path.join(music_dir, songs[rand]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

       

        elif 'email to Aashutosh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                if 'educational' in query:
                    to=Dict[1]
                else:
                    to=Dict[0]
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I'm facing an issue in sending this Email ")  