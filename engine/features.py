from playsound import playsound
import eel


@eel.expose
# Playing assistant sound function
def playAssistantSound():
    music_dir = "web//assets//audio//start_sound.mp3"
    playsound(music_dir)
