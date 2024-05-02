import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

def generate(prompt, model="gpt-3.5-turbo", temperature=0, max_tokens=150):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        messages=[
            {
                "role":"user",
                "content":prompt,
            },
        ],
    )
    
    return response.choices[0].message.content

# prompt = "Buat query select"
# result = generate(prompt)
# print(result)