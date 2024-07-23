import requests  # Importing the requests library to handle HTTP requests
import json # Importing Json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the Emotion predict service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Headers required for the API request
    ED_response = requests.post(url, json = myobj, headers=header)  # Sending a POST request to the API with the text and headers
    return ED_response.text # Returning the response text from the API

'''
    formatted_response = json.loads(ED_response.text)
    if ED_response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif ED_response.status_code == 500:
        label = None
        score = None
    response = {'label': label, 'score': score}
    return response
'''