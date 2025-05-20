import requests
import json

def emotion_detector(text_to_analyse: str) -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_string = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_string, headers=header)
    emotions = pars_response(response)
    emotions["dominant_emotion"] = find_dominant_emotion(emotions)
    return emotions

def pars_response(response_text: str) -> dict:
    emotions = response_text.json()["emotionPredictions"][0]["emotion"]
    return emotions

def find_dominant_emotion(emotions: dict) -> str:
    return max(zip(emotions.values(), emotions.keys()))[1]
