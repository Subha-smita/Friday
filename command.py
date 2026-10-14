from genai import ask_ai
import speech_recognition as sr
import sounddevice as sd
import webbrowser
import pyttsx3
import time
import musicLibrary
from datetime import datetime

recognizer = sr.Recognizer()




WAKE_WORDS = ["friday", "fri day", "freddy", "fry day", "friend", "frida"]

def speak(text):
    engine = pyttsx3.init()
    #time.sleep(0.5)
    engine.setProperty("volume", 1.0)
    engine.say("... ..." + text)   
    engine.runAndWait()
    engine.stop()
    time.sleep(0.3)

def listen(seconds):
    data = sd.rec(int(seconds * 16000), samplerate=16000, channels=1, dtype="int16")
    sd.wait()
    return sr.AudioData(data.tobytes(), 16000, 2)

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Roger that mam. Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        speak("Roger that mam. Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "what is the time" in c or "what is the date" in c:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        current_date = now.strftime("%A, %d %B %Y")
        speak("It is " + current_time + " on " + current_date)

    elif "open wikipedia" in c:
        speak("Roger that mam. Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")

    elif c.startswith("play"):
        song=c.replace("play","",1).strip()
        if song in musicLibrary.music:
            speak("here is the song .Playing" + song)
            webbrowser.open(musicLibrary.music[song])

    elif c.startswith("search"):
        query=c.replace("search","",1).strip()
        speak("searching"+query)
        webbrowser.open("https://www.google.com/search?q="+query)

    elif "goodbye" in c or "stop" in c or "exit" in c:
        speak("Goodbye mam,have a great day")
        raise SystemExit

   # else:
    #    speak("Sorry mam, I heard " + c + " but I don't know that command")
    else:
        answer = ask_ai(c)
        print("friday:",answer)
        speak(answer)