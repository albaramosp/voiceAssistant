from googletrans import Translator


class TranslatorManagerException(Exception):
    def __init__(self, message):
        super().__init__(message)


class TranslatorManager:
    def __init__(self):
        self._translator = Translator()

    def translate(self, txt, lang):
        try:
            translation = self._translator.translate(txt, dest=lang)
            return translation.text
        except Exception as e:
            raise TranslatorManagerException(e)


