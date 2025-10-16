#import speech_recognition as sr # this id the api for google speech to text
import tempfile
import whisper
from app.settings import LLM_MODEL, LLM_BASE_URL, WHISPER_MODEL

# Carga del modelo una sola vez (importante para rendimiento)
model = whisper.load_model(WHISPER_MODEL)

async def transcribe_audio(file):
    """
    Transcribe an uploaded audio file using Whisper.
    Compatible with FastAPI's UploadFile.
    """
    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        contents = await file.read()
        temp_audio.write(contents)
        temp_audio_path = temp_audio.name

    # Transcripción usando el path al archivo temporal
    result = model.transcribe(temp_audio_path)
    return result["text"]