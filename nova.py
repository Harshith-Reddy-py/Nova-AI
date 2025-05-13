import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import pyjokes
import logging
import pywhatkit
# Initialize and configure logging
logging.basicConfig(filename="nova_log.txt", level=logging.INFO)

# Initialize the speech engine
engine = pyttsx3.init()

# Set a female voice (usually index 1 on Windows)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # Female voice
else:
    engine.setProperty('voice', voices[0].id)  # Fallback to default

# Store user queries for simple session memory
conversation_history = []

def speak(text):
    print(f"Nova: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Nova, your upgraded assistant. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except Exception as e:
            logging.warning(f"Listening error: {e}")
            speak("Sorry, I didn't catch that.")
            return "None"

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        logging.warning(f"Recognition error: {e}")
        speak("Sorry, could you please repeat?")
        return "None"
    return query.lower()

def suggest_commands():
    speak("Here are some things you can ask me:")
    suggestions = [
        "What is the time?",
        "Open Notepad",
        "Play music",
        "Open a website",
        "Search something",
        "Tell me a joke",
        "Shutdown or restart the system",
        "Show my history",
        "Exit"
    ]
    for s in suggestions:
        speak(s)

def play_music():
    speak("Which song would you like to play?")
    song = take_command()
    speak(f"Playing {song} on YouTube")
    pywhatkit.playonyt(song)

def main():
    wish_user()

    while True:
        query = take_command()

        if query == "None":
            continue

        conversation_history.append(query)

        if 'time' in query:
            time_str = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_str}")

        elif 'open notepad' in query:
            os.system('notepad')
            speak("Opening Notepad.")

        elif 'play music' in query:
            play_music()

        elif 'open website' in query:
            speak("Which website should I open?")
            site = take_command()
            if site != "None":
                webbrowser.open(f"https://{site}.com")
                speak(f"Opening {site}.com")

        elif 'search' in query:
            speak("What would you like to search?")
            search_query = take_command()
            if search_query != "None":
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                speak(f"Searching Google for {search_query}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown' in query:
            speak("Are you sure you want to shut down the system? Say yes or no.")
            confirm = take_command()
            if 'yes' in confirm:
                speak("Shutting down.")
                os.system("shutdown /s /f /t 0")
            else:
                speak("Shutdown cancelled.")

        elif 'restart' in query:
            speak("Are you sure you want to restart the system? Say yes or no.")
            confirm = take_command()
            if 'yes' in confirm:
                speak("Restarting.")
                os.system("shutdown /r /f /t 0")
            else:
                speak("Restart cancelled.")

        elif 'history' in query:
            if conversation_history:
                speak("Here’s your recent history:")
                for item in conversation_history[-5:]:
                    speak(item)
            else:
                speak("There's nothing in history yet.")

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            speak("Goodbye! Have a productive day.")
            break

        else:
            speak("I didn't understand that.")
            suggest_commands()

if __name__ == "__main__":
    main()
