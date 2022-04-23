#########################################################################
#
#                           VOICE ASSISTANT
#                           ---------------
#   This module implements a voice assistant using pyttsx3 library.
#   This is a TTS library with which the assistant will process commands.
#
#
#
#########################################################################



from assistant import Assistant
from user import User

assistant = Assistant()
user = User()

# Waits for user input
while True:
    words, exc = user.speak()
    print(exc)
    if exc != -1:
        continue
    words = words.lower()
    print("You said ", words)

    if "hey laura" in words or "hi laura" in words:
        assistant.listen()

        while True:
            words, exc = user.speak()
            print(exc)
            if exc != -1:
                continue
            words = words.lower()
            print("You said ", words)

            if "time" in words:
                assistant.askTime()
            elif "date" in words:
                assistant.askDate()
            elif "weather" in words and "today" in words:
                assistant.askWeather("today")
            elif "weather" in words and "tomorrow" in words:
                assistant.askWeather("tomorrow")
            elif "turn off" in words or "bye" in words:
                print("Bye!")
                quit()
            else:
                assistant.speak("sorry, I didn't understand you")
            break
