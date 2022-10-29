'''
    Translates word in the English <--> French pair
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def extract_translated_word(watson_response):
    '''
        Extracts translated word given the API response
    '''
    return watson_response['translations'][0]['translation']

def translate(source_lan, target_lan, text):
    '''
        Translate a word given the source/target languages and
        the text to be translated
    '''
    translation = language_translator.translate(
    text=text,
    model_id=f'{source_lan}-{target_lan}').get_result()
    return extract_translated_word(translation)

def french_to_english(french_text):
    '''
        Translate a word from French to English
    '''
    return translate('fr','en',french_text)

def english_to_french(english_text):
    '''
        Translate a word from English to French
    '''
    return translate('en','fr',english_text)



def main():
    '''
        Main function
    '''
    print(english_to_french("house"))
    print(french_to_english('maison'))

if __name__ == '__main__':
    main()
