"""Flask server for emotion detection web app."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Render the main page (index.html)."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection():
    """
    Handle the emotion detection request.

    Returns:
        str: A formatted string with emotion scores or error message.
    """
    text_to_analyze = request.values.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
