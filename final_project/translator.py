"""
Provide some translator functions
"""
import json
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates english to french
    """
    frenchtranslation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    This function translates french to english
    """
    englishtranslation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return englishtranslation.get("translations")[0].get("translation")
