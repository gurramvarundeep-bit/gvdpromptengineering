from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

#llm = ChatOpenAI()
llm = ChatOllama(model="mistral:latest")

print(llm.invoke("tell me a joke of Allu Arjun").content)