from selenium.webdriver.chrome.options import Options
import time
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def sp(text):
    # Initialize the pyttsx3 speech synthesis engine
    engine = pyttsx3.init()

    # Adjust speech rate (speed) - values range from 0 to 200
    engine.setProperty('rate', 150)  # You can adjust this value to set the desired speech rate

    # Adjust voice tone (pitch) - values range from 0 to 1
    engine.setProperty('pitch', 0.8)  # You can adjust this value to set the desired voice tone

    # Speak the provided text
    engine.say(text)
    engine.runAndWait()


def speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source, timeout=8)
    try:
        print("Recognizing..")
        query = recognizer.recognize_google(audio, language="en")
        print("You said:", query)
        return query.lower()
    except Exception as e:
        print(e)
        return ""


# Define your speech_recognition function here if it's not imported
def play_song(song_name, driver):
    # Find the button associated with the specified song
    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//h2[contains(text(), '{song_name}')]/following-sibling::audio/following-sibling::div[@class='controls']/button[@class='play']"))
    )
    play_button.click()


def main_execution(query):
    query_str = str(query).lower()

    if "hello" in query_str or "log in" in query_str or "start" in query_str or "bhuvan" in query_str:
        # Use the global chrome_options object

        sp("hello there, I am opera ")
        sp("")
        options = Options()
        options.add_experimental_option("detach", True)

        # Use the ChromeDriverManager to automatically download and install the appropriate Chromedriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
       
        
        # Assuming you have a function login() for logging in with username and password
        if "opear" in query_str or "songs" in query_str:
            options = Options()
            options.add_experimental_option("detach", True)

        # Use the ChromeDriverManager to automatically download and install the appropriate Chromedriver
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            driver.get("http://127.0.0.1:5500/main.html")
            driver.maximize_window()

            sp("Welcome")
            while True:
                u = speech_recognition()
                if "play" in u or "song" in u:
                    sp("Which song would you like to play, sir?")
                    song_query = speech_recognition()
                    song_name = str(song_query).strip().lower()

                    # Switch case for song playback
                    if "heat waves" in song_name:
                        play_song("HEAT waves", driver)
                    elif "beliver" in song_name:
                        play_song("BELIVER", driver)
                    elif "on my way" in song_name:
                        play_song("ON MY WAY", driver)
                    elif "alone" in song_name:
                        play_song("Alone Pt II", driver)
                    elif "cartoon" in song_name:
                        play_song("Cartoon on on", driver)
                    elif "on my way" in song_name:
                        play_song("ON MY WAY", driver)
                    elif "murder in mind" in song_name:
                        play_song("MURDER IN MIND", driver)
                    elif "let me love you" in song_name:
                        play_song("Let Me Love You", driver)
                    elif "khairiyat bonus track" in song_name:
                        play_song("Khairiyat Bonus Track", driver)
        


while True:
    print("")
    query = speech_recognition()
    main_execution(query)
