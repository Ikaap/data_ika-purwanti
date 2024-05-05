import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["NAGA_AI_API_KEY"]
client = OpenAI(
    api_key=api_key,
    base_url="https://api.naga.ac/v1"
    )

def generate(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role":"user",
                "content":prompt,
            },
        ],
    )
    
    return response.choices[0].message.content