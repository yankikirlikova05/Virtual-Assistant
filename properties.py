import datetime
import calendar
import random

class Properties:
    def __init__(self):
        self.GREETING_INPUTS = ['hello','what is up','hey there']
        self.GREETING_RESPONSES = ['hi sir','hey sir','hello sir','yes sir']

    def getDate(self,):
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

    def greeting(self,text):
        for word in text.split():
            if word.lower() in self.GREETING_INPUTS:
                return random.choice(self.GREETING_RESPONSES)+"."

        return ''


    def getPerson(self,text):
        wordList = text.split()
        for i in range(0,len(wordList)):
            if i+3<=len(wordList)-1 and wordList[i].lower() == 'who' and  wordList[i+1].lower() == 'is':
                return wordList[i+2]+' '+wordList[i+3]