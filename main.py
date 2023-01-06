

from assistant.assistant import Assistant
from user.user import User

assistant = Assistant(user=User())
assistant.main_loop()

