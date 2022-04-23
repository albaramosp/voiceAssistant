from typing import AsyncContextManager
import pyttsx3
import datetime
from strings.strings_en import *
from config import *
from utils import *


class Assistant:
    """
    A voice assistant 

    Attributes
    ----------
    engine : Engine
        a TTS engine

    Methods
    -------
    speak(txt)
        Sets a text for the engine to say
    """

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('voice', 'english+f2')


    def listen(self):
        """
        Listens for user input, sending a sound signal to indicate it's listening.
        """
        import os
        duration = 0.3  # seconds
        freq = 440  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


    def speak(self, txt):
        """
        Sets a text for the engine to say.

        Parameters
        ----------
        txt : (str), the text that the engine will say.
        """

        self.engine.say(txt)
        self.engine.runAndWait()
    

    def askDate(self):
        """
        Asks today's date to assistant.
        """
        today = datetime.datetime.now()

        self.speak(CURRENT_DATE(today.strftime("%A"), today.strftime("%-d"), today.strftime("%B"), today.strftime("%Y")))


    def askTime(self):
        """
        Asks current time to assistant.
        """
        
        today = datetime.datetime.now()
        self.speak(CURRENT_TIME(today.strftime("%-I"), today.strftime("%-M"), today.strftime("%p")))


    def greet(self):
        """
            Greet user and ask for command.
        """
        today = datetime.datetime.now()

        if today.hour >= 6 and today.hour <= 12:
            self.speak(GREETING_MORNING)
        elif today.hour > 12 and today.hour <= 18:
            self.speak(GREETING_AFTERNOON)
        elif today.hour > 18 and today.hour <= 21:
            self.speak(GREETING_EVENING)
        else:
            self.speak(GREETING_NIGHT)
    
    
    def askWeather(self, day):
        forecast = get_forecast()
        now = datetime.datetime.now().hour

        if day == "today":
            forecast = forecast[0]
            
            if now >= 6 and now <= 12:
                cielo = forecast['estadoCielo'][3]['value']
            elif now > 12 and now <= 18:
                cielo = forecast['estadoCielo'][4]['value']
            elif now > 18 and now <= 21:
                cielo = forecast['estadoCielo'][5]['value']
            else:
                cielo = forecast['estadoCielo'][6]['value']
        else:
            forecast = forecast[1]
            cielo = forecast['estadoCielo'][0]['value']
        
        tmp_max = forecast['temperatura']['maxima']
        tmp_min = forecast['temperatura']['minima']

        try:
            cielo = SKY_STATUS[cielo]
        except:
            cielo = "unknown"

        self.speak(day + " we will have a temperature between " + \
            str(tmp_min) + " and " + str(tmp_max) + " degrees Celsius with " + \
                cielo + " skies")
        

        
        
    