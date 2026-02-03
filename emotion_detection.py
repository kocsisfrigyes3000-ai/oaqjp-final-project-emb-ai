import requests

# Watson NLP Emotion API endpoint
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

# Required header (model to use)
HEADERS = {
    "Content-Type": "application/json",
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def analyze_emotion(text_to_analyse: str):
    # Input payload for the API
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Call API
    response = requests.post(URL, headers=HEADERS, json=payload)
    response.raise_for_status()   # throw error if request fails

    data = response.json()

    # Extract emotion scores from the Watson API response
    emotions = data["emotionPredictions"][0]["emotion"]

    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    # Determine the dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return result in required format
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }


# Example usage
result = analyze_emotion("I am so happy and excited about today!")
print(result)
