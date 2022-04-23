import requests
from config import AEMET_KEY
import geocoder
import pandas as pd
from os import getcwd
import json

def get_forecast():
    """
    Get the weather forecast of the current location.
    """

    # Get city code from INE
    df = pd.read_excel(getcwd() + '/ine.xlsx', engine='openpyxl', skiprows=1)
    r = df.loc[df['NOMBRE '].str.contains(geocoder.ip('me').city)]
    cprov = str(r.iloc[0]['CPRO']).zfill(2)
    cmun = str(r.iloc[0]['CMUN']).zfill(3)

    url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/" +\
        cprov + cmun + "/?api_key=" + AEMET_KEY

    response = requests.get(url)

    if response.status_code == 200:
        url = response.json()['datos']
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()[0]['prediccion']['dia']
