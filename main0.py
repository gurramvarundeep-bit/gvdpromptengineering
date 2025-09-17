import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Initialize the language model
llm = ChatOpenAI(model="gpt-4o-mini")
#llm = OllamaLLM(model="mistral:latest")

def create_chain(prompt_template):
    prompt = PromptTemplate.from_template(prompt_template)
    return prompt | llm

# direct_task_prompt = """Classify the sentiment of the following text as positive, negative, or neutral.
# Do not explain your reasoning, just provide the classification.
# Text: {text}

# Sentiment:"""

# direct_task_chain = create_chain(direct_task_prompt)

# # Test the direct task specification
# texts = [
#     "I absolutely loved the movie! The acting was superb.",
#     "The weather today is quite typical for this time of year.",
#     "I'm disappointed with the service I received at the restaurant."
# ]

# for text in texts:
#     result = direct_task_chain.invoke({"text": text})
#     print(f"Text: {text}")
#     print(f"Sentiment: {result}")





# # Format Specification Prompting

# format_spec_prompt = """Generate a short news article about {topic}. 
# Structure your response in the following format:

# Headline: [A catchy headline for the article with in 5 words]

    # Lead: [A brief introductory paragraph summarizing the key points]

    # Body: [2-3 short paragraphs providing more details]

    # Conclusion: [A concluding sentence or call to action]"""

    # format_spec_chain = create_chain(format_spec_prompt)

    # # Test the format specification prompting
    # topic = "gold prices in the apac region"
    # result = format_spec_chain.invoke({"topic": topic})
    # print(result.content)






# Multi-step Reasoning Approach

multi_step_prompt = """Analyze the following text for its main argument, supporting evidence, and potential counterarguments. 
Provide your analysis in the following steps:

1. Main Argument: Identify and state the primary claim or thesis.
2. Supporting Evidence: List the key points or evidence used to support the main argument.
3. Potential Counterarguments: Suggest possible objections or alternative viewpoints to the main argument.

Text: {text}

Analysis:"""

multi_step_chain = create_chain(multi_step_prompt)

# Test the multi-step reasoning approach
text = """While electric vehicles are often touted as a solution to climate change, their environmental impact is not as straightforward as it seems. 
The production of batteries for electric cars requires significant mining operations, which can lead to habitat destruction and water pollution. 
Moreover, if the electricity used to charge these vehicles comes from fossil fuel sources, the overall carbon footprint may not be significantly reduced. 
However, as renewable energy sources become more prevalent and battery technology improves, electric vehicles could indeed play a crucial role in combating climate change."""

result = multi_step_chain.invoke({"text": text})
print(result.content)