from voice.listener import listen
from core.intents import handle_command
from voice.speaker import speak


def main():

    speak("Neuro OS initialized and ready")

    while True:

        command = listen()

        if command == "":
            continue

        if "stop" in command or "exit" in command:
            speak("Shutting down Neuro OS")
            break

        handle_command(command)


if __name__ == "__main__":
    main()