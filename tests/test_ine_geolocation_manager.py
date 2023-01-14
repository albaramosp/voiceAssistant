import unittest
from unittest import mock

from geolocation_manager.ine_geolocation_manager import INEGeolocationManager, GeolocationManagerException


class MockGeocoder:
    def __init__(self, fake_city, status_code, error):
        self.city = fake_city
        self.status_code = status_code
        self.error = error


def mocked_geocoder_ok(*args, **kwargs):
    return MockGeocoder('Sevilla', 200, None)


def mocked_geocoder_ko(*args, **kwargs):
    return MockGeocoder('unexisting', 404, "Location not found")


def mocked_geocoder_no_ine(*args, **kwargs):
    return MockGeocoder('Paris', 200, None)


class TestINEGeolocationManager(unittest.TestCase):
    @mock.patch('geocoder.ip', side_effect=mocked_geocoder_ok)
    def test_geolocation_ok(self, mocked_geocoder_ip):
        sut = INEGeolocationManager()
        expected = {
            'province_code': '41',
            'city_code': '91'
        }
        self.assertEqual(sut.get_geolocation(), expected)

    @mock.patch('geocoder.ip', side_effect=mocked_geocoder_ko)
    def test_geolocation_ko(self, mocked_geocoder_ip):
        sut = INEGeolocationManager()
        with self.assertRaises(GeolocationManagerException):
            sut.get_geolocation()

    @mock.patch('geocoder.ip', side_effect=mocked_geocoder_no_ine)
    def test_geolocation_no_ine(self, mocked_geocoder_ip):
        sut = INEGeolocationManager()
        with self.assertRaises(GeolocationManagerException) as context:
            sut.get_geolocation()
        self.assertTrue("Unable to locate in INE dataset" in context.exception.args[0])

