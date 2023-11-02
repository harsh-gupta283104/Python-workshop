import speech_recognition as sr
from gTTS import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

# Function to recognize speech and respond
def assistant():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).lower()
        print("You said:", user_input)

        if "hello" in user_input:
            speak("Hello! How can I assist you today?")

        # Add more commands and responses here

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("Sorry, I'm having trouble processing your request.")

if __name__ == "__main__":
    while True:
        assistant()
        