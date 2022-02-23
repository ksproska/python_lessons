# import biblioteki google tłumacza
from google_translator_simplified import Translator

while True:
    # pobranie tekstu z konsoli
    given_text = input("\nText in english to translate:   ")
    # pobranie tłumaczenia
    translation = Translator.get_translation('pl', given_text, 'en')
    # wyświetlenie tłumaczenia
    print(f'Translation                 :   {translation}')
