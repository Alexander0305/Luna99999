import pyttsx3

class TextToSpeech:
    def __init__(self, voice, rate):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
