import geocoder
import pandas as pd
import pathlib
import os
from interfaces.public import AbstractGeolocationManager


class INEGeolocationManager(AbstractGeolocationManager):

    def _get_geolocation(self):
        return geocoder.ip('me')

    def get_geolocation(self) -> dict:
        geolocation = self._get_geolocation()
        path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'ine.xlsx')
        df = pd.read_excel(path, engine='openpyxl', skiprows=1)
        r = df.loc[df['NOMBRE '] == geolocation.city]
        return {
            'province_code': str(r.iloc[0]['CPRO']),
            'city_code': str(r.iloc[0]['CMUN'])
        }
