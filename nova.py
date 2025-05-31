import os
import datetime
import random
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import pyjokes
import pywhatkit

# Supported voices (accents)
voices = ['en', 'en-uk', 'en-in', 'en-au']

# Sample weather reports
weather_reports = [
    "It's sunny with a high of 25 degrees.",
    "Cloudy skies and a chance of rain later today.",
    "Expect thunderstorms this evening. Stay safe!",
    "It's a cool day with light winds.",
    "Very hot today. Stay hydrated!"
]

# Smart chat responses
smart_responses = {
    "How are you": "I'm just a bunch of code, but I'm feeling fantastic!",
    "who are you": "I'm Nova, your AI assistant and friend!",
    "what is your name": "I'm Nova, always at your service!",
    "thank ": "You're always welcome!",
    "hello": "Hello there! Ready to help you.",
    "hi": "Hi! What can I do for you today?"
}

# Speak function using gTTS
def speak(text, lang='en'):
    print(f"Nova: {text}")
    tts = gTTS(text=text, lang=lang)
    tts.save("voice.mp3")
    os.system("mpg123 voice.mp3")

# Listen to user's command
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
    except Exception:
        print("Say that again please...")
        return "None"
    return query.lower()

# Check if query matches smart replies
def get_smart_reply(query):
    for key in smart_responses:
        if key in query:
            return smart_responses[key]
    return None

# Main Nova Assistant
def main():
    current_voice = 'en'  # Default voice (US)

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!", lang=current_voice)
    elif 12 <= hour < 18:
        speak("Good afternoon!", lang=current_voice)
    else:
        speak("Good evening!", lang=current_voice)
    speak("Hello! I am Nova, your personal assistant!", lang=current_voice)

    while True:
        query = take_command()

        if 'time' in query:
            time_str = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time_str}", lang=current_voice)

        elif 'weather' in query:
            weather = random.choice(weather_reports)
            speak(weather, lang=current_voice)

        elif 'open website' in query:
            speak("Which website would you like to open?", lang=current_voice)
            website = take_command()
            webbrowser.open(f"https://{website}.com")

        elif 'open google' in query:
            webbrowser.open('https://www.google.com')
            speak("Opening Google", lang=current_voice)

        elif 'search' in query:
            speak("What would you like to search for?", lang=current_voice)
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke, lang=current_voice)

        elif 'play song' in query or 'play music' in query:
            speak("Which song would you like to play?", lang=current_voice)
            song = take_command()
            speak(f"Playing {song} on YouTube", lang=current_voice)
            pywhatkit.playonyt(song)

        elif 'change voice' in query:
            current_voice = random.choice(voices)
            speak(f"Voice changed!", lang=current_voice)
            speak("Hello! This is Nova with a new voice.", lang=current_voice)

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! See you later!", lang=current_voice)
            break

        else:
            # Try smart reply
            smart_reply = get_smart_reply(query)
            if smart_reply:
                speak(smart_reply, lang=current_voice)
            elif query != "None":
                speak("Sorry, I didn't understand that.", lang=current_voice)

if __name__ == "__main__":
    main()

    
        


        
            
                
