from googletrans import Translator


class TranslatorManager:
    def __init__(self):
        self._translator = Translator()


    def translate(self, txt, lang):
        translation = self._translator.translate(txt, dest=lang)
        return translation.text

