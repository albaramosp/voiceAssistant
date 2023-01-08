import unittest
from unittest.mock import MagicMock, Mock

from translation_manager.translator_manager import TranslatorManager
from geolocation_manager.ine_geolocation_manager import INEGeolocationManager


class TestTranslatorManager(unittest.TestCase):
    def test_translation(self):
        manager = TranslatorManager()
        self.assertEqual(manager.translate(txt='ejemplo', lang='en'), 'example')

    def test_translation_unexisting_language(self):
        manager = TranslatorManager()
        with self.assertRaises(ValueError):
            manager.translate(txt='ejemplo', lang='unicorn')


class TestINEGeolocationManager(unittest.TestCase):
    class MockGeocoder:
        def __init__(self, fake_city):
            self.city = fake_city

    def test_geolocation(self):
        manager = INEGeolocationManager()
        manager._get_geolocation = Mock(return_value=self.MockGeocoder('Sevilla'))
        expected = {
            'province_code': '41',
            'city_code': '91'
        }
        self.assertEqual(manager.get_geolocation(), expected)
