from dotenv import load_dotenv
from os import getcwd, environ

load_dotenv(getcwd() + '/env_files/.env')

API_URL = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/"
API_KEY = environ.get("AEMET_KEY")