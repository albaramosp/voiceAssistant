import geocoder
import pandas as pd
import pathlib
import os
from interfaces.public import AbstractGeolocationManager


class INEGeolocationManager(AbstractGeolocationManager):
    def get_geolocation(self) -> dict:
        geolocation = geocoder.ip('me')
        path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'ine.xlsx')
        df = pd.read_excel(path, engine='openpyxl', skiprows=1)
        r = df.loc[df['NOMBRE '].str.contains(geolocation.city)]
        return {
            'province_code': str(r.iloc[0]['CPRO']),
            'city_code': str(r.iloc[0]['CMUN'])
        }
