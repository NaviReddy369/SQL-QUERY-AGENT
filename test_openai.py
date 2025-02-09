import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # ✅ Use the new package!

# Load API Key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM Model
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

print("✅ LangChain AI Model is Ready!")
