import datetime
import warnings
import wikipedia
from audio_process import Audio
from properties import Properties

warnings.filterwarnings('ignore')

# TESTS NEEDED IF THERE IS AN ERROR IN CLASSES
audio = Audio()
properties = Properties


while True:
    response = ''
    text = audio.recordAudio()

    if (audio.wakeWord(text) == True):

        response = response + properties.greeting(text)
        if('date' in text):
            get_date = properties.getDate()
            response = response + ' ' + get_date

        elif ('who is' in text):
            person = properties.getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        elif ('see you' in text):
            bye = 'okay sir, bye'
            response = response + ' '+bye
            audio.assistantResponse(response)
            break

        elif ('time' in text):
            now = datetime.datetime.now()
            hour = now.hour

            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

        # TEST NEEDED
        elif ('add wake word' in text):
            text.lower()
            audio.addWakeWord(text[14:-1])

            response = response+' '+'It is  '+str(hour)+':'+minute+' .'
        audio.assistantResponse(response)
