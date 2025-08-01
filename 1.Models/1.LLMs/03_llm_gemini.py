from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash', temperature = 0)
result = llm.invoke("Write a Poem on cricket")
print(result.content) 