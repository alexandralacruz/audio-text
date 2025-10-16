from models.local_llm import LocalLLM
from app.transcription import transcribe_audio
from app.settings import LLM_MODEL, LLM_BASE_URL, WHISPER_MODEL



class CorrectorAgent:
    def __init__(self, llm_model=LLM_MODEL, base_url=LLM_BASE_URL):
        self.llm = LocalLLM(llm_model, base_url)

    async def process_and_correct_audio(self, file):
        # Llama directamente a la función asíncrona
        text = await transcribe_audio(file)
        prompt = f"Correct grammar and improve clarity for this text: {text}"
        corrected = self.llm.generate(prompt)
        return {"original": text, "corrected": corrected}

    async def correct_text(self, text):
        prompt = f"Correct grammar and improve clarity for this text, put between ** errors: {text}"
        corrected = await self.llm.generate(prompt)
        return {"original": text, "corrected": corrected}