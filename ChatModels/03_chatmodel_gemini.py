from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model= "gemini-1.5-flash", google_api_key = os.getenv("GOOGLE_API_KEY"), temperature = 0)
result = model.invoke("How to play cricket?")
print(result.content)