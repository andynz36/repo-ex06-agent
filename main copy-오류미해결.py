import os
from dotenv import load_dotenv
from google import genai

# .env 읽기
load_dotenv()

# API 키 가져오기
key = os.getenv(
    "GEMINI_API_KEY"
)

# Gemini 연결
client = genai.Client(api_key=key)

# 질문하기
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="AI Agent를 중학생에게 설명해줘"
)

print(response.text)
