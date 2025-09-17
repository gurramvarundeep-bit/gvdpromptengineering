from pyexpat import model
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4.1-nano")
# llm = OllamaLLM(model="mistral:latest")

# write a function to invoke llm with question
def invoke_llm(question: str) -> str:
    response = llm.invoke(question)
    return response

translate_prompt_template = "Given text, translate from English to spanish"
classify_prompt_template = "Given text, classify it into one of the following categories: [positive, negative, neutral]"
code_gen_prompt_template = "Given text, generate python code if text is having #codegen# tag"
ai_coversation_prompt_template = "Given text, generate conversation as a AI assitant"
sql_generator_prompt_template = "Given text, generate sql query if text is having #sql# tag"
reasoning_prompt_template = "Given text, solve the problem in steps. first  identify all odd numbers and then sum them up"
        

if __name__ == "__main__":
    # Welcome to chatbot
    print("Welcome to chatbot")
    while True:
        question = input("Ask a question: ")
        # response = invoke_llm(question)
        response = invoke_llm(reasoning_prompt_template+" "+question)
        #print(response)
        print(response.content)
        if question == "exit":
            break

    # translate_prompt_template = "Given text, translate from English to spanish"
    # classify_prompt_template = "Given text, classify it into one of the following categories: [positive, negative, neutral]"
    # code_gen_prompt_template = "Given text, generate python code if text is having #codegen# tag"
    # ai_coversation_prompt_template = "Given text, generate conversation as a AI assitant"
    # sql_generator_prompt_template = "Given text, generate sql query if text is having #sql# tag"
    # reasoning_prompt_template = "Given text, solve the problem in steps. first  identify all odd numbers and then sum them up"
    # prompt = input("Enter a prompt: ")
    # response = invoke_llm(classify_prompt_template+" "+prompt)
    # response = invoke_llm(reasoning_prompt_template+" "+prompt)
    # print(response)