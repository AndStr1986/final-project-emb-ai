"""
Executing this function initiates the application of Emotion Detector
to be executed over the Flask channel and deployed on localhost:5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    This code rendeers the index.html template
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    This code receives the text from the HTML interface and runs emotion_detector
    over it using emotion_detector() function.
    The output returens a formated string with emotion scores and the
    dominate emotion
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_analyze)
    
    if emotion["dominant_emotion"] == None:
        return "Invalid text! Please try again!"
        
    return f"""For the given statement, the system response is
     'anger': {emotion['anger']},
     'disgust': {emotion['disgust']},
     'fear': {emotion['fear']}, 
     'joy': {emotion['joy']}, 
     'sadness': {emotion['sadness']}, 
     The dominant emotion is {emotion['dominant_emotion']}"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
