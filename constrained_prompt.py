from dotenv import load_dotenv
import prompt_template as pt
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import prompt_template as pt
import re

load_dotenv()


#llm = OllamaLLM(model="mistral:latest")
llm = ChatOpenAI(model="gpt-4o-mini")

# Function to display model outputs
def display_output(output):
    """Display the model's output in a formatted manner."""
    print("Model Output:")
    print("-" * 40)
    print(output)
    print("-" * 40)
    print(output)


# Generate the constrained output
input_variables = {
    "product": "smart water bottle",
    "target_audience": "health-conscious millennials",
    "tone": "casual and friendly",
    "word_limit": "75"
}

# chain = pt.constrained_prompt | llm
# output = chain.invoke(input_variables).content
# display_output(output)

# Generate the rule-based output
input_variables = {
    "job_title": "Senior Software Engineer",
    "company": "TechInnovate Solutions",
    "location": "San Francisco, CA",
    "experience": "5+"
}

# chain = pt.job_posting_prompt | llm
# output = chain.invoke(input_variables).content
# display_output(output)

# parse and clean output

def clean_output(output):
    for key, value in output.items():
        print(f"Processing {key}...")
        print(f"Value: {value}")
        if isinstance(value, str):
            # Remove leading/trailing whitespace and normalize newlines
            output[key] = re.sub(r'\n\s*', '\n', value.strip())
    return output

# # Generate the parsed output
chain = pt.parsed_job_posting_prompt | llm
raw_output = chain.invoke(input_variables).content

# # Parse and clean the output
parsed_output = pt.regex_parser.parse(raw_output)
cleaned_output = clean_output(parsed_output)

# Display the parsed output
print("Parsed Output:")
for key, value in cleaned_output.items():
    print(f"{key.upper()}:")
    print(value)
    print()


# Generate the constrained review
input_variables = {
    "product": "iphone 17",
    "rating": "4",
    "pros": "4",
    "cons": "3",
    "word_limit": "200"
}

chain = pt.review_prompt | llm
output = chain.invoke(input_variables).content
display_output(output)