"""
    Collection of english messages used by the system.
"""

# Greetings
GREETING_MORNING = "Good morning, how can I help you?"
GREETING_AFTERNOON = "Good afternoon, how can I help you?"
GREETING_EVENING = "Good evening, how can I help you?"
GREETING_NIGHT = "Good night, how can I help you?"

# Thank and welcome
THANKS = "Thank you"
WELCOME = "You're welcome"

# Dates and times
def CURRENT_DATE(weekday, day, month, year):
    return "Today is " + weekday + ", " + day + " of " + month + " " + year

def CURRENT_TIME(hour, minute, pm):
    return "It's " + hour + " " + minute + " " + pm


# VPN
def CONNECTING_TO_VPN(vpn):
    return "Connecting to " + vpn + " VPN"


# Unknown
UNKNOWN_COMMAND = "I'm sorry, I don't understand you. How can I help you?"
UNKNOWN_VPN = "Sorry, this VPN is not supported yet"