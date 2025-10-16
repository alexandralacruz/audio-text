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

    async def correct_text(self, text, detected_language_code):
        # Mapeo de códigos ISO a nombres legibles
        language_codes = {
            "en": "English",
            "fr": "French",
            "es": "Spanish",
            "de": "German",
            # agrega otros si necesitas
        }

        # Obtener nombre del idioma
        language = language_codes.get(detected_language_code, detected_language_code) 
        
        prompt = f"""
        You are a grammar corrector. 
        The following text is written in {language}.
        Correct grammar, spelling, and clarity in the same language. 
        Mark the corrected parts by placing - around the wrong words.

        Text:
        {text}
        """
        
        corrected = await self.llm.generate(prompt)
        return {"original": text, "corrected": corrected}