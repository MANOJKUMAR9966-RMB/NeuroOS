import webbrowser
import os


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_google():
    webbrowser.open("https://www.google.com")


def open_vscode():
    code_path = r"C:\Users\MANOJ KUMAR\AppData\Local\Programs\Microsoft VS Code\Code.exe"

    if os.path.exists(code_path):
        os.startfile(code_path)
    else:
        print("VS Code path not found")


# Testing directly
if __name__ == "__main__":
    open_youtube()