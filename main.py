import os
import platform
import eel
import webbrowser
from engine.features import *
from engine.command import takecommand

eel.init("web")

playAssistantSound()


def open_browser():
    url = "http://localhost:8000/index.html"
    if platform.system() == "Windows":
        os.system(f'start msedge.exe --app="{url}"')
    elif platform.system() == "Darwin":  # macOS
        os.system(f'open -a "Microsoft Edge" "{url}"')
    else:
        webbrowser.open(url)


# Open the browser
open_browser()

eel.start('index.html', mode=None, host='localhost', block=True)

while True:
    eel.sleep(1)  # Sleep for a short period to prevent high CPU usage
