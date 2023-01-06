"""
    Collection of english messages used by the system.
"""

ASK_COMMAND = "how can I help you?"

GREETING_MORNING = "Good morning, " + ASK_COMMAND
GREETING_AFTERNOON = "Good afternoon, " + ASK_COMMAND
GREETING_EVENING = "Good evening, " + ASK_COMMAND
GREETING_NIGHT = "Good night, " + ASK_COMMAND

THANKS = "Thank you"
WELCOME = "You're welcome"

def CURRENT_DATE(weekday, day, month, year):
    return "Today is " + weekday + ", " + day + " of " + month + " " + year

def CURRENT_TIME(hour, minute, pm):
    return "It's " + hour + " " + minute + " " + pm

def CONNECTING_TO_VPN(vpn):
    return "Connecting to " + vpn + " VPN"

def WEATHER_FORECAST(day, tmp_max, tmp_min, sky_status):
    return day + " we expect " + sky_status + " skies with temperatures between " + tmp_min + " and " + tmp_max + " degrees"

UNKNOWN_COMMAND = "I'm sorry, I don't understand you"
UNKNOWN_VPN = "Sorry, this VPN is not supported yet"
UNKNOWN = "Sorry, I'm unable to answer this right now. Please try again"

TODAY = "today"
TOMORROW = "tomorrow"