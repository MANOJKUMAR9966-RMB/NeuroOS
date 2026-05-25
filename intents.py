from automation.actions import (
    open_youtube,
    open_google,
    open_vscode
)

from voice.speaker import speak


def handle_command(command):

    if "open youtube" in command:
        speak("Opening YouTube")
        open_youtube()

    elif "open google" in command:
        speak("Opening Google")
        open_google()

    elif "open visual studio code" in command or "open vs code" in command:
        speak("Opening Visual Studio Code")
        open_vscode()

    else:
        speak("Sorry, I did not understand the command")