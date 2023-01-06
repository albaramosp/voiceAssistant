import requests
import geocoder
import pandas as pd
from os import getcwd
from . import settings
import datetime

class ForecastManager:
    @staticmethod
    def get_current_location() -> dict:
        return geocoder.ip('me')

    
    def _get_ine_city_province(self, city: str):
        """
        Transform city to INE's city and province codes.
        :param city: string with city name
        :return tuple with INE's city and province codes
        """
        df = pd.read_excel(getcwd() + '/ine.xlsx', engine='openpyxl', skiprows=1)
        r = df.loc[df['NOMBRE '].str.contains(city)]
        return r.iloc[0]['CPRO'], r.iloc[0]['CMUN']


    @staticmethod
    def _hour_to_period(hour: int) -> str:
        """
        Defines the next forecast period from an hour
        :param hour: hour of request
        :return next forecast period
        """
        if 6 < hour <= 12:
            period = '12-18'
        elif 12 < hour <= 18:
            period = '18-24'
        elif 18 < hour <= 24:
            period = '00-06'
        else:
            period = '06-12'
        
        return period


    def get_forecast(self, is_today: bool):
        """
        Get the weather forecast of the current location, 
        for current day or for tomorrow (currently supported dates).
        :param is_today: boolean indicating if forecast is for
        today or for tomorrow
        """
        tmp_max = tmp_min = sky_status = None
        location = self.get_current_location()
        cprov, cmun = self._get_ine_city_province(location.city)

        url = settings.API_URL + \
            str(cprov).zfill(2) + str(cmun).zfill(3) + \
            "/?api_key=" + settings.API_KEY
        
        response = requests.get(url)

        if response.status_code == 200:
            url = response.json()['datos']
            response = requests.get(url)

            if response.status_code == 200:
                forecasts = response.json()[0]['prediccion']['dia']
                target_date = datetime.datetime.now() if is_today \
                    else (datetime.datetime.now() + datetime.timedelta(days=1))
                target_period = self._hour_to_period(
                    target_date.hour) if is_today else '00-24'
                
                for forecast in forecasts:
                    if forecast['fecha'].split('T')[0] == target_date.strftime("%Y-%m-%d"):
                        tmp_max = forecast['temperatura']['maxima']
                        tmp_min = forecast['temperatura']['minima']

                        for sky in forecast['estadoCielo']:
                            if sky['periodo'] == target_period:
                                sky_status = sky['descripcion']
                                break
                        break

        return tmp_max, tmp_min, sky_status
