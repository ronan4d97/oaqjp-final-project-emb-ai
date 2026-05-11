import requests
import json


def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detection API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extract the emotion scores from the response
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    
    # Extract individual emotion scores
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    
    # Get the emotion corresponding to the dominant score
    dominant_emotion = max(emotions, key=emotions.get)  
    
    # Prepare the final answer as a dictionary containing all emotion scores and the dominant emotion
    final_answer = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
    
    return final_answer
