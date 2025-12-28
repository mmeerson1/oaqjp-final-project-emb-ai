''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        string_response = 'Invalid text! Please try again!'
    else:
        string_response = f"For the given statement, the system response is \
        'anger':{str(response['anger'])}, \
        'disgust':{str(response['disgust'])}, \
        'fear':{str(response['fear'])}, \
        'joy':{str(response['joy'])} \
        and sadness':{str(response['sadness'])}. \
        The dominant emotion is <b>{response['dominant_emotion']}</b>."
    return string_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
