import os
from dotenv import load_dotenv  
import requests

load_dotenv()  # Load environment variables from .env file
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization" : f"Bearer {GROQ_API_KEY}",
    "Content-Type" : "application/json"
}

request = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who am I in spiritual terms?"}
    ]
}

response = requests.post(url, headers=headers, json=request)
print(response.json().get("choices")[0].get("message").get("content"))
print('No of tokens used is ' + str(response.json().get('usage').get('total_tokens')))