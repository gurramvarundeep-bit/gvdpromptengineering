from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

prompt = PromptTemplate.from_template("tell me a joke of {subject}")

chain = prompt | llm

print(chain.invoke({"subject": "dog"}).content)
