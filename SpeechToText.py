from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1

url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/cefb9631-a052-4f28-8426-3868a1f53322"
iam_apikey_s2t = "wI9I9DIiUQ-GzGKm49tW4Q1X1qF-TjwkS1G9OC2zoAsB"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)

filename='/home/kandurh@perceptive.cloud/DataScience/Meenu_DataScience.mp3'
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
var = response.result
print(var)
from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)