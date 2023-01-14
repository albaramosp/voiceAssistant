import speech_recognition as sr


class User:
    """
    A class used to represent a user of the assistant

    Attributes
    ----------
    engine : Engine
        a TTS engine

    Methods
    -------
    speak: str
        Sets a text for the engine to say
    """

    def __init__(self):
        self._recognizer = sr.Recognizer()

    def speak(self):
        """
        Wait for user commands
        """

        with sr.Microphone() as source:
            self._recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self._recognizer.listen(source)

        try:
            audio = self._recognizer.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + audio)
            exception = -1
        except sr.UnknownValueError as e:
            print("Google Speech Recognition could not understand audio: ", e)
            exception = 1
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            exception = 2
        
        return audio, exception
