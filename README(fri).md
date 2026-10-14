# Friday: Voice Assistant

Friday is a Python-based voice assistant that listens to spoken commands and responds with speech. It automates everyday tasks such as web searches, opening applications, telling the time, and answering general queries, all hands-free.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example Commands](#example-commands)
- [Configuration](#configuration)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## Features

- **Voice recognition:** captures and converts spoken commands to text.
- **Text-to-speech:** responds to the user with a natural-sounding voice.
- **Web search:** searches Google, YouTube, and Wikipedia by voice.
- **System tasks:** opens applications and websites on command.
- **Date and time:** announces the current date and time.
- **Greeting and small talk:** wishes the user based on the time of day.
- **Modular design:** commands are easy to add or modify.


---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.x |
| Speech recognition | `SpeechRecognition` |
| Text-to-speech | `pyttsx3` |
| Web automation | `webbrowser`, `pywhatkit` |
| Information retrieval | `wikipedia` |
| Utilities | `datetime`, `os` |
|Text file|`requirements.txt`.

---

## Project Structure



friday/
├── main.py              # Entry point: listens for voice input and routes it
├── command.py           # Handles and executes user commands
├── genai.py             # Generative AI integration for conversational responses
├── musicLibrary.py      # Music collection used by the music commands
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation



---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A working microphone
- An internet connection (required for speech recognition and web features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/friday-voice-assistant.git
   cd friday-voice-assistant
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

> **Note:** If `PyAudio` fails to install, install it with `pip install pipwin && pipwin install pyaudio` (Windows) or `sudo apt install portaudio19-dev && pip install pyaudio` (Linux).

---

## Usage

Run the assistant from the project directory:

```bash
python main.py
```

Friday will greet you and start listening. Speak clearly after the prompt, and say **"exit"** or **"stop"** to shut it down.

---

## Example Commands

| Say this | Friday does this |
|---|---|
| "What's the time?" | Announces the current time |
| "Open YouTube" | Opens YouTube in your browser |
| "Search Wikipedia for Python" | Reads out a short Wikipedia summary |
| "Play [song name]" | Plays the song on YouTube |
| "Exit" | Closes the assistant |



---

## Configuration

- **Voice:** change the voice, rate, or volume through the `pyttsx3` engine properties in `main.py`.
- **Wake word / name:** edit the assistant name in the configuration section of the code.
- **Language:** change the `language` parameter in the recognizer call to support other languages.

---

## Future Improvements

- Integrate an LLM for natural, conversational responses
- Add a wake-word detection feature ("Hey Friday")
- Build a GUI for visual feedback
- Support email, calendar, and reminder automation
- Add multilingual support
- Add weather and news updates

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## Author

**Subhasmita Tripathy**
B.Tech in Computer Science Engineering, NIST University


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
