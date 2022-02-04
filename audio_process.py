import speech_recognition as sr
from gtts import gTTS
import os


class Audio():
    def __init__(self):
        self.wake_words = ['jarvis', 'friday',
                           'computer', 'friend', 'assistant']

    def recordAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)

        data = ' '

        try:
            data = r.recognize_google(audio)
            print("You said: "+data)

        except sr.UnknownValueError:
            print(
                "Google speech recognition could not understand the audio, unknown error.")

        except sr.RequestError as e:
            print('Requestresults from Google Speech Recognition service error: ', e)

        return data

    def assistantResponse(self, text):
        print(text)
        myobj = gTTS(text=text, lang='en', slow=False)
        myobj.save('assistant_response.mp3')
        os.system('open assistant_response.mp3')

    def wakeWord(self, text):
        text = text.lower()

        for phrase in self.wake_words:
            if phrase in text:
                return True

        return False

    def addWakeWord(self, word):
        self.wake_words.append(word)
