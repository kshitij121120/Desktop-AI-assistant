import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import numpy as np
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)

    except Exception as e:
        print("Sorry!, say it again")
        return "None"
    return query


if __name__=="__main__":

    speak('Hii! I am FRIDAY')

    query = takecommand().lower()

    if 'wikipedia' in query:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'the time' in query:
        strfTime = datetime.datetime.now().strftime("%H:%M")
        print(f"The time is {strfTime}")
        speak(f"The time is {strfTime}")

    elif 'open youtube' in query:
        webbrowser.open("www.youtube.com")
        
    elif 'search youtube' in query:
        speak("OK! Please give your search query")
        result = takecommand()
        codepath = 'https://www.youtube.com/results?search_query='+ result
        speak("Here is your video")
        os.startfile(codepath)


    elif 'open netflix' in query:
        webbrowser.open("https://www.netflix.com/")

    elif 'play music' in query:
        music_dir = 'C:\\Users\\hp\\Music\\New Songs'
        songs = os.listdir(music_dir)
        print(songs)
        arr = np.random.randint(0,4)
        print(arr)
        os.startfile(os.path.join(music_dir,songs[arr]))

    elif 'open word' in query:
        codepath = "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        os.startfile(codepath)

    elif 'open chrome' in query:
        codepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        os.startfile(codepath)

    elif 'google' in query:
        speak("What do you want to search")
        result = takecommand()
        codepath = 'https://www.google.com/search?q='+ result
        os.startfile(codepath)