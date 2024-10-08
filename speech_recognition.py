import speech_recognition as sr

class SpeechRecognition:
    def __init__(self, engine, language):
        self.engine = engine
        self.language = language
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language=self.language)
                return text
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return None
            except sr.RequestError as e:
                print(f"Error: {e}")
                return None
