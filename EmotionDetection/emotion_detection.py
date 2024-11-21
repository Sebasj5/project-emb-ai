import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    if response.status_code == 200:
        emotion_data =response.json()   
        
        anger_score = emotion_data['emotion']['anger']
        disgust_score = emotion_data['emotion']['disgust']
        fear_score = emotion_data['emotion']['fear']
        joy_score = emotion_data['emotion']['joy']
        sadness_score = emotion_data['emotion']['sadness']
        
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy' : joy_score,
            'sadness' : sadness_score
        }
        
        domination_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy' : joy_score,
            'sadness' : sadness_score,
            'dominant emotion': domination_emotion
        }

    else: 
        return {"error": "Error en la solicitud" + str(response.status_code)}
    
    
    
    
if __name__ == "__main__":
    test_text = "I love this new technology."
    result = emotion_detector(test_text)
    print(result)
    
    