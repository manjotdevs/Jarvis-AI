import speech_recognition as sr
import sys
import webbrowser
import os
from variables import *

recognizer = sr.Recognizer()
browser_name = "firefox"


def get_user_input():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=6)
            print("Recognizing...")
            audio_output = recognizer.recognize_google(audio)
            print(f"User said: {audio_output}")
            return audio_output.lower()  # Return the recognized audio in lower case
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
            return None
        except sr.WaitTimeoutError:
            print("Sorry, you did not speak within the time limit.")
            return None
def quit_command(audio_output):
    if audio_output.lower() == "quit":
        print("Goodbye!")
        sys.exit()

def browser_input(audio_output):
    if audio_output.lower()[0] == "open":
        for website in websites:
            if website[0].lower() in audio_output.lower():
                webbrowser.open(website[1])


def software_input(audio_output):
   for software in softwares:
        if software[0].lower() in audio_output.lower():
            os.system(software[1])

def serach_input(audio_output):
    if audio_output.lower() == "youtube search":
        youtube_query = audio_output.split()[2]
        print(youtube_query)
        youtube_search = "https://www.youtube.com/results?search_query="
        for youtube in youtube_query:
            youtube_search += youtube + "+"
            webbrowser.open(youtube_search)
            print(f"Youtube search: {youtube_search}")

def main():
    while True:
        try:
            audio_output = get_user_input()
            if audio_output:
                browser_input(audio_output)
                software_input(audio_output)
                quit_command(audio_output)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
