from openai import OpenAI
from app.core.config import settings


class MetisLLM:
    def __init__(self):
        self.client = OpenAI(
           api_key=settings.METIS_API_KEY,
           base_url=settings.METIS_BASE_URL 
        )

    def generate(self,prompt: str , temperature: float = 0.2)->str:

        response = self.client.chat.completions.create(
            model=settings.METIS_MODEL,
            messages=[
                {
                    'role':'system',
                    'content':(
                        "You are a helpful AI assistant. "
                        "Answer accurately and concisely"
                    )
                },
                {
                    'role':'user',
                    'content':prompt
                }
            ],
            temperature=temperature
        )
        return response.choices[0].message.content