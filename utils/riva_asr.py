import riva.client

def transcribe_audio(audio_path):
    try:
        auth = riva.client.Auth(uri="localhost:50051")
        asr_service = riva.client.ASRService(auth)
        config = riva.client.RecognitionConfig(language_code="en-US", enable_automatic_punctuation=True)
        with open(audio_path, "rb") as audio_data:
            response = asr_service.offline_recognize(audio_data, config)
        if response.results:
            return response.results[0].alternatives[0].transcript
        return "No transcript detected"
    except:
        return "Mock Transcript: Let's schedule a meeting next Tuesday at 3 PM."
