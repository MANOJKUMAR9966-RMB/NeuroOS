import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            command = command.lower()

            print(f"You said: {command}")

            return command

        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""

        except sr.RequestError:
            print("Speech Recognition service error")
            return ""


# Test directly
if __name__ == "__main__":
    text = listen()
    print(text)