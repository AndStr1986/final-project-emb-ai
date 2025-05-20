import requests

def emotion_detector(text_to_analyse: str) -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_string = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_string, headers=header)
    return response.text
