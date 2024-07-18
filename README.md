# Opera: Voice-Controlled Music Player using Selenium and Python

## Overview

Opera is a voice-controlled music player application that uses Python libraries such as Selenium, pyttsx3, and SpeechRecognition to enable users to control music playback on a web interface through voice commands. This project integrates voice recognition and web automation to create a seamless, hands-free music control experience.

## Key Components

### Voice Synthesis (pyttsx3)
- Provides feedback to the user by converting text to speech.
- Adjustable speech rate and pitch to enhance user interaction.

### Speech Recognition (SpeechRecognition and sr)
- Captures and processes voice commands using the Google Web Speech API.
- Recognizes various commands like "play", "pause", and specific song names.

### Web Automation (Selenium)
- Automates browser actions to control the music player on a web page.
- Utilizes `webdriver_manager` for managing ChromeDriver installations.

### Web Interface
- A user-friendly HTML/CSS-based dashboard for displaying and controlling the music player.
- Includes controls for play, pause, and volume adjustment.

## Main Functionalities

### Speech-to-Text Conversion
- Listens for voice commands and translates them into text for further processing.

### Voice Feedback
- Provides auditory responses to the user's commands, enhancing the interactive experience.

### Web Interaction
- Navigates to the web-based music player.
- Automates playback controls based on user commands.

### Song Selection and Playback
- Recognizes specific song titles and initiates playback accordingly.
- Handles various songs and provides options for different playback controls.

## Execution Flow

### Initialization
- Starts by greeting the user and providing initial instructions.

### Voice Command Handling
- Continuously listens for voice commands.
- Responds to "hello", "log in", and other start commands.

### Music Playback
- Asks the user for the song name upon receiving a relevant command.
- Plays the selected song by interacting with the web interface.

## Implementation

Using the Python library `pyttsx3` (Python Text to Speech version 3), the application converts text to speech to provide auditory feedback to the user.

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/opera-voice-controlled-music-player.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd opera-voice-controlled-music-player
    ```


3. **Run the application:**
    ```bash
    python main.py


    ```
3. **Install pyttsx3:**
 ```bash
 pip install pyttsx3 
 pip install Selenium 
 ```
These pakages will be the main requirments for the project.
5. ****
## Requirements

- Python 3.x
- Selenium
- pyttsx3
- SpeechRecognition
- WebDriver Manager for Chrome
Install all the above requirments in your IDE





## Acknowledgements

Special thanks to the developers and the community for their valuable libraries and tools that made this project possible.

## Contact

For any inquiries or feedback, please contact akashleeswamy@gmail.com
