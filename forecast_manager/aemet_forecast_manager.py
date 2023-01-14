import requests
from interfaces.public import AbstractForecastManager, ForecastManagerException
import datetime
from forecast_manager import settings


class AemetForecastManager(AbstractForecastManager):
    def __init__(self, province_code: str, city_code: str):
        self._api_url = settings.AEMET_API_URL + \
            province_code.zfill(2) + city_code.zfill(3) + \
            "/?api_key=" + settings.AEMET_API_KEY

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

    def get_forecast(self, target_date: datetime) -> dict:
        tmp_max = tmp_min = sky_status = None
        response = requests.get(self._api_url)

        if response.status_code != 200:
            raise ForecastManagerException("Error requesting AEMET API")

        url = response.json()['datos']
        response = requests.get(url)

        if response.status_code != 200:
            raise ForecastManagerException("Error requesting AEMET API")

        forecasts = response.json()[0]['prediccion']['dia']
        today = datetime.datetime.now().date
        target_period = self._hour_to_period(
            target_date.hour) if today == target_date else '00-24'

        for forecast in forecasts:
            if forecast['fecha'].split('T')[0] == target_date.strftime("%Y-%m-%d"):
                tmp_max = forecast['temperatura']['maxima']
                tmp_min = forecast['temperatura']['minima']

                for sky in forecast['estadoCielo']:
                    if sky['periodo'] == target_period:
                        sky_status = sky['descripcion']
                        break
                break

        return {
            'tmp_max': tmp_max,
            'tmp_min': tmp_min,
            'sky_status': sky_status
        }
