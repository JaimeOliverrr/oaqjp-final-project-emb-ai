'''
Emotion detector function in web application development.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    '''
    Calling emotion detector function through the web application.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    string =  ', '.join(f"'{k}': {v}" for k, v in response.items() if k != 'dominant_emotion')
    dominant = response['dominant_emotion']
    return f"For the given statement, the system response is {string}. The dominant emotion is <b>{dominant}</b>."

@app.route("/")
def render_index_page():
    '''
    Index page.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

