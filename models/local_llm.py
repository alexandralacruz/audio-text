import json
import httpx
from app.settings import LLM_MODEL, LLM_BASE_URL


class LocalLLM:
    def __init__(self, model=LLM_MODEL, base_url=LLM_BASE_URL):
        self.model = model
        self.url = f"{base_url}/api/generate"

    async def generate(self, prompt):
        async with httpx.AsyncClient() as client:
            async with client.stream("POST", self.url, json={"model": self.model, "prompt": prompt}) as response:
                full = ""
                async for line in response.aiter_lines():
                    if line:
                        data = json.loads(line)
                        full += data.get("response", "")
                return full