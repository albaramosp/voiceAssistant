from dotenv import load_dotenv
from os import getcwd, environ

load_dotenv(getcwd() + '/env_files/.env')

AEMET_API_URL = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/"
AEMET_API_KEY = environ.get("AEMET_KEY")