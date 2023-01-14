from abc import abstractmethod, ABC
import datetime


class GeolocationManagerException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ForecastManagerException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class AbstractForecastManager(ABC):
    @abstractmethod
    def get_forecast(self, target_date: datetime) -> dict:
        """
        Get weather forecast information from a given source
        for a specific date and period. 
        Weather information may include, for example, maximum
        and minimum temperatures, sky status, precipitation, etc.
        :param target_date: date and time to forecast
        :return dict with forecast information
        """
        ...


class AbstractGeolocationManager(ABC):
    @abstractmethod
    def get_geolocation(self) -> dict:
        """
        Get user geolocation and return location's information,
        such as city, province, etc.
        :return dict with location information
        """
        ...