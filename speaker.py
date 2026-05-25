import pyttsx3

engine = pyttsx3.init()

# Voice settings
engine.setProperty('rate', 170)   # Speed
engine.setProperty('volume', 1.0) # Volume


def speak(text):
    print(f"NeuroOS: {text}")
    engine.say(text)
    engine.runAndWait()


# Testing directly
if __name__ == "__main__":
    speak("Neuro OS speaker module initialized successfully")