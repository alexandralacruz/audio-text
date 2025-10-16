from fastapi import FastAPI, UploadFile
from app.transcription import transcribe_audio
from app.agent import CorrectorAgent
from app.settings import LLM_MODEL, LLM_BASE_URL, WHISPER_MODEL
app = FastAPI()
agent = CorrectorAgent(llm_model=LLM_MODEL, base_url=LLM_BASE_URL)

@app.post("/process_audio")
async def process_audio(file: UploadFile):
    text = await transcribe_audio(file)
    corrected = await agent.correct_text(text)
    #response = response(corrected)
    return {"original": text, "corrected": corrected}

@app.post("/correct-text")
async def correct_text(text: str):
    result = await agent.correct_text(text)
    return result

@app.post("/correct-audio")
async def correct_audio(file: UploadFile):
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    result = agent.process_and_correct_audio(file_path)
    return result