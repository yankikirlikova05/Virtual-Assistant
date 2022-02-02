import speech_recognition as sr 
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    data = ' '

    try:
        data = r.recognize_google(audio)
        print("You said: "+data)

    except sr.UnknownValueError:
        print("Google speech recognition could not understand the audio, unknown error.")

    except sr.RequestError as e :
        print('Requestresults from Google Speech Recognition service error: ',e)

    return data


def assistantResponse (text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save('assistant_response.mp3')
    os.system('open assistant_response.mp3')


def wakeWord(text):
    wake_words=['jarvis','friday','computer','friend','assistant']
    text=text.lower()

    for phrase in wake_words:
        if phrase in text:
            return True

    return False

def getDate():
    now=datetime.datetime.now() 
    my_date = datetime.datetime.today()
    weekday= calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January','February','March','April','May','June','July','August','September','October'
    ,'November','December']
    ordinal_numbers=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
    '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th',
    '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th',
    '29th', '30th', '31st']
    return 'Today is '+weekday+' '+month_names[monthNum-1]+' the '+ordinal_numbers[dayNum-1]

def greeting(text):
    GREETING_INPUTS =['hello','what is up','hey there']
    GREETING_RESPONSES = ['hi sir','hey sir','hello sir','yes sir']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)+"."

    return ''


def getPerson(text):
    wordList = text.split()
    for i in range(0,len(wordList)):
        if i+3<=len(wordList)-1 and wordList[i].lower() == 'who' and  wordList[i+1].lower() == 'is':
            return wordList[i+2]+' '+wordList[i+3]


while True:
    response = ''
    text = recordAudio()

    if (wakeWord(text)== True):

        response= response + greeting(text)     
        if('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences = 2)
            response = response + ' ' + wiki
        if ('see you' in text):
            bye = 'okay sir, bye'
            response = response + ' '+bye
            assistantResponse(response)
            break

        if ( 'time' in text):
            now = datetime.datetime.now()
            hour=now.hour

            if now.minute<10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response=response+' '+'It is  '+str(hour)+':'+minute+' .'
        assistantResponse(response)
