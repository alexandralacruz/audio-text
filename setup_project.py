# setup_project.py
# This script automatically creates the folder structure, boilerplate files, and Docker setup for the audio agent project.

import os

folders = [
    'app',
    'models',
    'tests',
    'data',
    'notebooks'
]

files = {
    'app/__init__.py': '',
    'app/main.py': '''from fastapi import FastAPI, UploadFile
from app.transcription import transcribe_audio
from app.correction import correct_text
from app.agent import respond

app = FastAPI()

@app.post("/process_audio")
async def process_audio(file: UploadFile):
    text = await transcribe_audio(file)
    corrected = correct_text(text)
    response = respond(corrected)
    return {"original": text, "corrected": corrected, "agent_response": response}
''',

    'app/transcription.py': '''import speech_recognition as sr

async def transcribe_audio(file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file.file) as source:
        audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data)
''',

    'app/correction.py': '''def correct_text(text):
    # Placeholder for local LLM or rule-based grammar fix
    return text.replace("i", "I") if text.startswith("i ") else text
''',

    'app/agent.py': '''def respond(text):
    return f"Got it! Here's your improved text: {text}"
''',

    'app/utils.py': '''# Helper functions will go here
''',

    'models/__init__.py': '',

    'models/local_llm.py': '''class LocalLLM:
    def __init__(self):
        pass

    def correct(self, text: str) -> str:
        return f"[LLM corrected] {text}"
''',

    'tests/__init__.py': '',

    'tests/test_transcription.py': '''def test_transcription_placeholder():
    assert True
''',

    'requirements.txt': '''fastapi
uvicorn
speechrecognition
transformers
torch
openai-whisper
''',

    'README.md': '''Audio Agent Project
===================
This project provides an end-to-end pipeline for:
1. Receiving audio input.
2. Transcribing speech to text.
3. Correcting grammar via a local LLM.
4. Returning the refined response through an API or notebook.

Run locally:
------------
1. Install dependencies: `pip install -r requirements.txt`
2. Launch API: `uvicorn app.main:app --reload`
3. Test endpoint: `POST /process_audio` with an audio file.

Docker Setup:
-------------
1. Build the image: `docker build -t audio-agent .`
2. Run the container: `docker-compose up`
3. Access API at: `http://localhost:8000`
''',

    'Dockerfile': '''# Use official Python base image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
''',

    'docker-compose.yml': '''version: '3.9'
services:
  audio-agent:
    build: .
    container_name: audio_agent_api
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    restart: always
''',

    'notebooks/demo_agent.ipynb': '',
}

def create_project():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for path, content in files.items():
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created file: {path}")

    print("\n✅ Project structure and Docker setup successfully created!")

if __name__ == '__main__':
    create_project()