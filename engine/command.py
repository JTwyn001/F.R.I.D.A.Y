import os
import eel
import speech_recognition as sr
import pyttsx3

eel.init('web')


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()


@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, 10, 6)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""
        except Exception as e:
            print("Listening exception: " + str(e))
            return ""

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""
    return query.lower()


if __name__ == "__main__":
    eel.start('index.html', block=False)
    while True:
        text = takecommand()
        if text:
            print(f"Executing command: {text}")
            os.system(text)  # Be careful with os.system, as it will execute any command (potential security risk)
        eel.sleep(1)

# text = takecommand()

# os.system(text)
