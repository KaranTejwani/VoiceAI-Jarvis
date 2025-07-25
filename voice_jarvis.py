import speech_recognition as sr
from playsound import playsound
import time

WAKE_WORD = "hey jarvis"
OUTPUT_FILE = "command.txt"

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen_for_wake_word():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for wake word...")
        while True:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")
                if WAKE_WORD in text:
                    print("Wake word detected!")
                    return
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                continue

def record_command():
    with mic as source:
        print("Listening for your command...")
        audio = recognizer.listen(source, phrase_time_limit=8)
        return audio

def recognize_and_save(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized command: {text}")
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Command saved to {OUTPUT_FILE}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def main():
    while True:
        listen_for_wake_word()
        audio = record_command()
        recognize_and_save(audio)
        print("Say 'Hey Jarvis' to give another command.")
        time.sleep(1)

if __name__ == "__main__":
    main() 