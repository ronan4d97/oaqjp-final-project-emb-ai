# Importing necessary flask modules
from flask import Flask, render_template, request

# Importing the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the final string as per the assessment
        for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze") # get the text from the HTML interface
    analysis_result = emotion_detector(text_to_analyze) # run the emotion detection function on the text
    
    if analysis_result["dominant_emotion"] is None:
        return "Invalid input! Try again."
    
    # Construct the final string to be returned as output
    final_string = "For the given statement, the system response is "
    for emotion, value in analysis_result.items():
        if emotion == "dominant_emotion":
            continue
        final_string += f"'{emotion}': {value}, "
    final_string = final_string.rstrip(", ")
    final_string += f". The dominant emotion is {analysis_result['dominant_emotion']}."

    return final_string

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html") # render the index.html page

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000, debug=True)
