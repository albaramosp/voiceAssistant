from translation_manager.translator_manager import TranslatorManager, TranslatorManagerException
import unittest
from unittest import mock


class TestTranslatorManager(unittest.TestCase):
    def test_translation(self):
        manager = TranslatorManager()
        self.assertEqual(manager.translate(txt='ejemplo', lang='en'), 'example')

    def test_translation_unexisting_language(self):
        manager = TranslatorManager()
        with self.assertRaises(TranslatorManagerException) as e:
            manager.translate(txt='ejemplo', lang='unicorn')