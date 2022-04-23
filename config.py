from dotenv import load_dotenv
from os import getcwd, environ

load_dotenv(getcwd() + '/env_files/.env')

AEMET_KEY = environ.get("AEMET_KEY")