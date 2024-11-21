"""
This module contains the Flask server for the emotion detection application.
It includes routes for processing text and returning emotion analysis results.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}), 400

    emotions = emotion_detector(text_to_analyze)
    
    if emotions["dominant_emotion"] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    return jsonify(emotions)

if __name__ == '__main__':
    app.run(debug=True)