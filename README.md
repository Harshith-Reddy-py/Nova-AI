**Nova: Offline-Capable Intelligent Voice Assistant**

**Overview:**
Nova is an intelligent voice assistant developed using Python, designed to operate without reliance on internet APIS. It offers a friendly female voice, assisting users in managing their systems, browsing the web, telling jokes, and more.

### 📦 Requirements
To run Nova, ensure you have installed Python 3.7 or higher. Then, install the necessary Python packages:

```bash
# Install dependencies
pip install pyttsx3 speechrecognition pyjokes pyaudio
```

If you encounter issues when installing `pyaudio`, try the following commands:

```bash
pip install pipwin
pipwin install pyaudio
```

### 🛠 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Nova.git
   cd Nova
   ```
2. Launch Nova:
   ```bash
   python nova_windows.py
   ```

### 🔧 Functionality
- **Voice Recognition:** Utilizes the `speech_recognition` library to listen and interpret voice commands.
- **Text-to-Speech:** Employs `pyttsx3` to produce speech output in a female voice.
- **Humour:** Implements `pyjokes` for offline jokes and entertainment.
- **System Commands:** Executes application launches and commands through built-in Python modules.

### 🧠 Example Commands
- “What’s the time?”
- “Open Notepad”
- “Play music”
- “Open website”
- “Search Python tutorials”
- “Tell me a joke”
- “Shutdown the system”
- “Restart the computer”

### 🧩 Future Development Ideas
- Implement alarm and reminder functionalities.
- Integrate a wake word feature (e.g., “Hey Nova”).
- Develop a graphical user interface (GUI) version.
- Convert the application into an executable (.exe) for desktop use.

### 🤖 Voice Customisation
By default, Nova uses a female voice on Windows. To change the voice, you may use the following code:

```python
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Typically selects a female voice
```
To explore available voices, you can print their names using `print(voice.name)`.

### 📝 License
This project is open-source and licensed under the MIT License.

### 🙌 Credits
Developed by Harshith Reddy. Contributions, forks, and issue reports are welcome!




