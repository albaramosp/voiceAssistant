import geocoder
import pandas as pd
import pathlib
import os
from interfaces.public import AbstractGeolocationManager, GeolocationManagerException


class INEGeolocationManager(AbstractGeolocationManager):
    def get_geolocation(self) -> dict:
        geolocation = geocoder.ip('me')
        if geolocation.status_code != 200:
            raise GeolocationManagerException(geolocation.error)
        path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'ine.xlsx')
        df = pd.read_excel(path, engine='openpyxl', skiprows=1)

        try:
            r = df.loc[df['NOMBRE '] == geolocation.city]
            return {
                'province_code': str(r.iloc[0]['CPRO']),
                'city_code': str(r.iloc[0]['CMUN'])
            }
        except Exception:
            raise GeolocationManagerException("Unable to locate in INE dataset")


