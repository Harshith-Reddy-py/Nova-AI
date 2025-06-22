#NOVA-AI

**🌟 Overview:**
Meet Nova – your smart voice assistant! Built using Python, Nova functions without needing internet APIs. With a friendly female voice, she'll help you manage system tasks, browse the web, share jokes, and much more.

### 📦 Requirements
To get started with Nova, ensure that you have Python 3.7 or later installed. Next, install the required Python packages:

```bash
# Install dependencies
pip install pyttsx3 speechrecognition pyjokes pyaudio pywhatkit
```

If you run into issues installing `pyaudio`, use these commands instead:

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
- **Voice Recognition:** Powered by the `speech_recognition` library, Nova listens and interprets your voice commands seamlessly.
- **Text-to-Speech:** Using `pyttsx3`, Nova speaks back in a warm, female voice.
- **Humour:** Enjoy offline jokes courtesy of the `pyjokes` library.
- **System Commands:** Nova can open applications and execute commands right from your Python code!

### 🧠 Example Commands
- “What’s the time?”
- “Open Notepad”
- “Play some music”
- “Open a website”
- “Search for Python tutorials”
- “Tell me a joke”
- “Shutdown the system”
- “Restart the computer”

### 🧩 Future Development Ideas
- Add alarm and reminder features.
- Introduce a wake word functionality (e.g., “Hey Nova”).
- Create a graphical user interface (GUI).
- Package the application as an executable (.exe) for easy desktop access.

### 🤖 Voice Customisation
By default, Nova uses a female voice on Windows. To switch voices, use:

```python
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Generally selects a female voice
```

Explore available voices by printing their names with `print(voice.name)`.

### 📝 License
This project is open-source and operates under the MIT License.

### 🙌 Credits
Created by Harshith Reddy. Contributions, forks, and feedback are always welcome!
