#from genai import ask_ai
import speech_recognition as sr
import sounddevice as sd
from command import speak,processCommand

recognizer = sr.Recognizer()



WAKE_WORDS = ["friday", "fri day", "freddy", "fry day", "friend", "frida"]

#speak

def listen(seconds):
    data = sd.rec(int(seconds * 16000), samplerate=16000, channels=1, dtype="int16")
    sd.wait()
    return sr.AudioData(data.tobytes(), 16000, 2)

#processCommand

if __name__ == "__main__":
    speak("Initializing Friday. How can I help you?")
    print("Friday is activated.")

    while True:
        try:
            print("Say 'Friday'...")
            word = recognizer.recognize_google(listen(3)).lower()

            if any(w in word for w in WAKE_WORDS):
                speak("..Yes mam,I am up")
                print("Speak your command now...")
                command = recognizer.recognize_google(listen(5))
                print("Command:", command)
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand, try again")
        except sr.RequestError as e:
            print("Service error:", e)
        except Exception as e:
            print("Error:", repr(e))