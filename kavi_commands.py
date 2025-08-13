import os
import webbrowser
import pyautogui

def run_command(query):
    query = query.lower()

    if "open notepad" in query:
        os.system("notepad.exe")
        return "Opening Notepad."

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "open calculator" in query:
        os.system("calc.exe")
        return "Opening Calculator."

    elif "screenshot" in query or "take screenshot" in query:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return "Screenshot taken and saved as screenshot.png."

    elif "open cmd" in query or "open command prompt" in query:
        os.system("start cmd")
        return "Opening Command Prompt."

    elif "open paint" in query:
        os.system("mspaint.exe")
        return "Opening Paint."

    elif "shutdown" in query:
        return "Sorry, I won’t do that. It’s too dangerous."

    else:
        return None
