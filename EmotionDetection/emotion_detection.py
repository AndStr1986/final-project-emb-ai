"""
Package to request from watson-emotion
"""
import requests

def emotion_detector(text_to_analyse: str) -> str:
    """
    fucntion that requests from watson-emotion API an emotion respons based on text
    output is a dict
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_string = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_string, headers=header, timeout=20)
    emotions = pars_response(response)
    emotions["dominant_emotion"] = find_dominant_emotion(emotions)
    return emotions

def pars_response(response_text: str) -> dict:
    """
    This funciton takes in a text string, converts it to json
    And returns a subset of the json file
    """
    emotions = response_text.json()["emotionPredictions"][0]["emotion"]
    return emotions

def find_dominant_emotion(emotions: dict) -> str:
    """
    This function takes in a dict, swaps the values from value to key and key to value.
    so that we can use the max() function to return the the dominant emotion
    outputs a string of the dominant emotion
    """
    return max(zip(emotions.values(), emotions.keys()))[1]
