from utils.riva_asr import transcribe_audio as riva_transcribe

def transcribe_audio(audio_path):
    return riva_transcribe(audio_path)
