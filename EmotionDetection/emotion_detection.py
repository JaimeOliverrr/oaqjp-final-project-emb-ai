import requests  # Importing the requests library to handle HTTP requests
import json # Importing Json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the Emotion predict service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Headers required for the API request
    ED_response = requests.post(url, json = myobj, headers=header)  # Sending a POST request to the API with the text and headers
    if ED_response.status_code == 400: # Error handling
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions
    formatted_response = json.loads(ED_response.text) # Formatting text response using Json
    emotions = formatted_response['emotionPredictions'][0]['emotion'] # Keeping only the selected emotions list/dictionary
    dominant = max(emotions, key=emotions.get) # Finding dominant emotion
    emotions['dominant_emotion'] = dominant # Adding dominant emotion statement.
    return emotions
