from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

prompt = PromptTemplate.from_template("tell me a joke of {subject}")

class ResponseFormatter(BaseModel):
    """Always use this tool to structure your response to the user."""
    answer: str = Field(description="The answer to the user's question")
    followup_question: str = Field(description="A followup question the user could ask")
    queries: str = Field(description="A list of queries that the user could ask")

llm = ChatOpenAI()

model_with_structure = llm.with_structured_output(ResponseFormatter)


chain = prompt | model_with_structure 

print(chain.invoke({"subject": "future of agentic ai"}))

