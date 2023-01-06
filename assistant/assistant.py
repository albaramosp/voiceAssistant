import pyttsx3
import datetime
from assistant.strings_en import *
from os import system
from forecast_manager.forecast_manager import ForecastManager
from translation_manager.translator_manager import TranslatorManager
from . import settings
from user.user import User


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

    def __init__(self, user: User):
        self._user = user
        self._wake_commands = ['hey laura', 'hi laura']
        self._duration = 0.3 # seconds
        self._frequency = 440 # Hz
        self._rate = 180 # voice speed

        self._engine = pyttsx3.init()
        self._engine.setProperty('rate', self._rate)
        self._engine.setProperty('voice', 'english+f2')


    def _speak(self, txt: str):
        """
        Sets a text for the engine to say.

        :param txt: str to say
        """

        self._engine.say(txt)
        self._engine.runAndWait()
    

    def _beep(self):
        system('play -nq -t alsa synth {} sine {}'.format(self._duration, self._frequency))


    def _greet(self):
        """
        Greet user and ask for command.
        """
        today = datetime.datetime.now()

        if 6 < today.hour <= 12:
            self._speak(GREETING_MORNING)
        elif 12 < today.hour <= 18:
            self._speak(GREETING_AFTERNOON)
        elif 18 < today.hour <= 20:
            self._speak(GREETING_EVENING)
        else:
            self._speak(GREETING_NIGHT)
    

    def _is_waking_up_command(self, txt: str) -> bool:
        """
        Checks if the text contains the commands
        to wake up assistant.
        :param txt: text with commands
        :return True if text contains waking up commands,
        False in another case
        """

        return any(map(txt.__contains__, self._wake_commands))


    def _tell_date(self):
        today = datetime.datetime.now()

        self._speak(CURRENT_DATE(today.strftime("%A"),
                                today.strftime("%-d"),
                                today.strftime("%B"),
                                today.strftime("%Y")))


    def _tell_time(self):       
        today = datetime.datetime.now()
        self._speak(CURRENT_TIME(today.strftime("%-I"),
                   today.strftime("%-M"), today.strftime("%p")))


    def _tell_error(self):
        self._speak(UNKNOWN_COMMAND)


    def _tell_weather(self, is_today: bool):
        tmp_max, tmp_min, sky = ForecastManager().get_forecast(is_today)
        
        if tmp_max is not None and tmp_min is not None and sky is not None:
            sky = TranslatorManager().translate(sky, settings.LANGUAGE)
            self._speak(WEATHER_FORECAST(day=TODAY if is_today else TOMORROW,
                        tmp_max=str(tmp_max), tmp_min=str(tmp_min), sky_status=sky))
        else:
            self._speak(UNKNOWN)


    def main_loop(self):
        # Waits for user input
        while True:
            print("Say hey/hi laura to wake up the assistant")
            words, exc = self._user.speak()
            if exc != -1:
                continue
            words = words.lower()

            if self._is_waking_up_command(words):
                self._beep()
                print("Tell your command after listening appears")

                while True:
                    words, exc = self._user.speak()
                    if exc != -1:
                        continue
                    command = words.lower()

                    if "time" in command:
                        self._tell_time()
                    elif "date" in command:
                        self._tell_date()
                    elif all(map(command.__contains__, ["weather", "today"])):
                        self._tell_weather(is_today=True)
                    elif all(map(command.__contains__, ["weather", "tomorrow"])):
                        self._tell_weather(is_today=False)
                    elif any(map(command.__contains__, ["bye", "turn off"])):
                        print("Bye!")
                        quit()
                    else:
                        self._tell_error()
                    break

        
    

        
        

        
        
    