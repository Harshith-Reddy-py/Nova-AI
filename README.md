🔊 Nova - Your Personal Offline Voice Assistant (Windows)
Nova is an intelligent, offline-capable voice assistant built with Python. She listens, responds with a friendly female voice, and helps you manage your system, browse the web, tell jokes, and more — without requiring internet APIs.

✨ Features
🎤 Voice-Controlled: Just speak — no need to type.

👩‍🦰 Human-like Female Voice (Windows).

🕐 Tells current time.

📝 Opens Notepad on command.

🎵 Plays local music.

🌐 Opens websites or performs Google searches.

😂 Tells funny jokes using pyjokes.

💻 Executes system commands (shutdown/restart).

🧠 Remembers recent queries during the session.

🔒 100% offline — no API keys required.



📦 Requirements
Ensure you have Python 3.7+ installed. Then install the required Python packages:

bash
Copy
Edit

pip install pyttsx3 speechrecognition pyjokes pyaudio
If you get an error installing pyaudio, try this:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
📁 Project Structure
bash
Copy
Edit
Nova/
│
├── nova_windows.py      # Main assistant code
├── README.md            # You're reading it!
├── nova_log.txt         # Auto-generated log file
└── assets/              # (Optional) Add demo media here
🛠 Setup Instructions
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/Nova.git
cd Nova

Run Nova:

bash
Copy
Edit
python nova_windows.py
🔧 How It Works
Uses speech_recognition to listen and process your voice.

Uses pyttsx3 for text-to-speech with a female voice.

Uses pyjokes for offline humor.

Opens apps and performs commands using built-in Python modules.


🧠 Example Commands
“What’s the time?”

“Open Notepad”

“Play music”

“Open website”

“Search Python tutorials”

“Tell me a joke”

“Shutdown the system”

“Restart the computer”

🧩 To-Do / Future Ideas
Add alarm/reminder functionality

Integrate wake word (e.g., “Hey Nova”)

Build a GUI version

Convert to .exe desktop app

🤖 Voice Customization
Nova uses a female voice by default on Windows. If you want to change it:

python
Copy
Edit
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Usually female
Use the voice index or print(voice.name) to explore installed voices.

📝 License
This project is open-source and available under the MIT License.

🙌 Credits
Created by Harshith Reddy
Feel free to contribute, fork, or report issues!
