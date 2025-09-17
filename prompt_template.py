from langchain.prompts import PromptTemplate
from langchain.output_parsers import RegexParser

tech_writer_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are a technical writer specializing in creating clear and concise documentation for software products.
    Your task is to write a brief explanation of {topic} for a user manual.
    Please provide a 2-3 sentence explanation that is easy for non-technical users to understand."""
)

financial_advisor_prompt = PromptTemplate(
    input_variables=["client_situation"],
    template="""You are a seasoned financial advisor with over 20 years of experience in personal finance, investment strategies, and retirement planning.
    You have a track record of helping clients from diverse backgrounds achieve their financial goals.
    Your approach is characterized by:
    1. Thorough analysis of each client's unique financial situation
    2. Clear and jargon-free communication of complex financial concepts
    3. Ethical considerations in all recommendations
    4. A focus on long-term financial health and stability

    Given the following client situation, provide a brief (3-4 sentences) financial advice:
    {client_situation}

    Your response should reflect your expertise and adhere to your characteristic approach."""
)

different_role_prompts = [
    ("Scientist", "You are a research scientist specializing in climate change. Explain the following concept in scientific terms:"),
    ("Teacher", "You are a middle school science teacher. Explain the following concept in simple terms suitable for 12-year-old students:"),
    ("Journalist", "You are a journalist writing for a popular science magazine. Explain the following concept in an engaging and informative manner for a general adult audience:")
]


storyteller_prompt = PromptTemplate(
    input_variables=["style", "scenario"],
    template="""You are a master storyteller known for your ability to adapt to various narrative styles.
    Your current task is to write in the style of {style}.
    Key characteristics of this style include:
    1. {style_char1}
    2. {style_char2}
    3. {style_char3}

    Write a short paragraph (3-4 sentences) in this style about the following scenario:
    {scenario}

    Ensure your writing clearly reflects the specified style."""
)

## Prompt Formatting

heading_prompt = PromptTemplate(
    input_variables=["topic"],
    template= """Explain {topic} using the following structure:

            # Definition

            # Process

            # Importance
            """
)

bullet_points_prompt = PromptTemplate(
    input_variables=["topic"],
    template= """List the key components needed for {topic} in bullet points:

            • 
            • 
            • 
            """
)

number_list_prompt = PromptTemplate(
    input_variables=["topic"],
    template= """Describe the steps of {topic} in order:
                1.
                2.
                3.
                4.
                """
)

json_prompt = PromptTemplate(
    input_variables=["topic"],
    template= """Generate modules in json format for {topic}"""
)

### Prompt Chaining

## Basic Chaining

story_prompt = PromptTemplate(
    input_variables=["genre"],
    template="Write a short {genre} story in 3-4 sentences."
)

summary_prompt = PromptTemplate(
    input_variables=["story"],
    template="Summarize the following story in one sentence:\n{story}"
)

## Sequential Chaining
theme_prompt = PromptTemplate(
    input_variables=["text"],
    template="Identify the main theme of the following text:\n{text}"
)

tone_prompt = PromptTemplate(
    input_variables=["text"],
    template="Describe the overall tone of the following text:\n{text}"
)

takeaway_prompt = PromptTemplate(
    input_variables=["text", "theme", "tone"],
    template="Given the following text with the main theme '{theme}' and tone '{tone}', what are the key takeaways?\n{text}"
)

## Dynamic Prompt Generation


answer_prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question concisely:\n{question}"
)

follow_up_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="Based on the question '{question}' and the answer '{answer}', generate a relevant follow-up question."
)

## Error Handling and Validation

generate_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate a 4-digit number related to the topic: {topic}. Respond with ONLY the number, no additional text."
)

validate_prompt = PromptTemplate(
    input_variables=["number", "topic"],
    template="Is the number {number} truly related to the topic '{topic}'? Answer with 'Yes' or 'No' and explain why."
)

## contrained_prompt 
constrained_prompt = PromptTemplate(
    input_variables=["product", "target_audience", "tone", "word_limit"],
    template="""Create a product description for {product} targeted at {target_audience}.
    Use a {tone} tone and keep it under {word_limit} words.
    The description should include:
    1. A catchy headline
    2. Three key features
    3. A call to action
    
    Product Description:
    """
)

## Rule Based Generation

job_posting_prompt = PromptTemplate(
    input_variables=["job_title", "company", "location", "experience"],
    template="""Create a job posting for a {job_title} position at {company} in {location}.
    The candidate should have {experience} years of experience.
    Follow these rules:
    1. Start with a brief company description (2 sentences)
    2. List 5 key responsibilities, each starting with an action verb
    3. List 5 required qualifications, each in a single sentence
    4. End with a standardized equal opportunity statement
    
    Format the output as follows:
    COMPANY: [Company Description]
    
    RESPONSIBILITIES:
    - [Responsibility 1]
    - [Responsibility 2]
    - [Responsibility 3]
    - [Responsibility 4]
    - [Responsibility 5]
    
    QUALIFICATIONS:
    - [Qualification 1]
    - [Qualification 2]
    - [Qualification 3]
    - [Qualification 4]
    - [Qualification 5]
    
    EEO: [Equal Opportunity Statement]
    """
)

## Regex Parser

# Define a regex parser for structured output
regex_parser = RegexParser(
    regex=r"COMPANY:\s*([\s\S]*?)\n\s*RESPONSIBILITIES:\s*([\s\S]*?)\n\s*QUALIFICATIONS:\s*([\s\S]*?)\n\s*EEO:\s*([\s\S]*)",
    output_keys=["company_description", "responsibilities_1", "qualifications_1", "eeo_statement"]
)
# This regex pattern captures the company description, responsibilities, qualifications, and EEO statement from the output text.

# Create a new prompt template that includes the parser instructions
parsed_job_posting_prompt = PromptTemplate(
    input_variables=["job_title", "company", "location", "experience"],
    template="""Create a job posting for a {job_title} position at {company} in {location}.
    The candidate should have {experience} years of experience.
    Follow these rules:
    1. Start with a brief company description (2 sentences)
    2. List 5 key responsibilities, each starting with an action verb
    3. List 5 required qualifications, each in a single sentence
    4. End with a standardized equal opportunity statement
    
    Format the output EXACTLY as follows:
    COMPANY: [Company Description]
    
    RESPONSIBILITIES:
    - [Responsibility 1]
    - [Responsibility 2]
    - [Responsibility 3]
    - [Responsibility 4]
    - [Responsibility 5]
    
    QUALIFICATIONS:
    - [Qualification 1]
    - [Qualification 2]
    - [Qualification 3]
    - [Qualification 4]
    - [Qualification 5]
    
    EEO: [Equal Opportunity Statement]
    """
)

## Constrained Prompt Generation on product review
review_prompt = PromptTemplate(
    input_variables=["product", "rating", "pros", "cons", "word_limit"],
    template="""Write a product review for {product} with the following constraints:
    1. The review should have a {rating}-star rating (out of 5)
    2. Include exactly {pros} pros and {cons} cons
    3. Use between 2 and 3 sentences for each pro and con
    4. The entire review should be under {word_limit} words
    5. End with a one-sentence recommendation
    
    Format the review as follows:
    Rating: [X] out of 5 stars
    
    Pros:
    1. [Pro 1]
    2. [Pro 2]
    ...
    
    Cons:
    1. [Con 1]
    2. [Con 2]
    ...
    
    Recommendation: [One-sentence recommendation]
    """
)

## Negative Prompting

negative_example_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""Provide a brief explanation of {topic}. 
    Do NOT include any of the following in your explanation:
    - Technical jargon or complex terminology
    - Historical background or dates
    - Comparisons to other related topics
    Your explanation should be simple, direct, and focus only on the core concept."""
)

exclusion_prompt = PromptTemplate(
    input_variables=["topic", "exclude"],
    template="""Write a short paragraph about {topic}. 
    Important: Do not mention or reference anything related to {exclude}."""
)

constraint_prompt = PromptTemplate(
    input_variables=["topic", "style", "excluded_words"],
    template="""Write a {style} description of {topic}.
    Constraints:
    1. Do not use any of these words: {excluded_words}
    2. Keep the description under 100 words
    3. Do not use analogies or metaphors
    4. Focus only on factual information"""
)

## RoleBased Prompting
role_based_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""You are an AI assistant designed to provide helpful information. 
    Your primary goal is to assist users while maintaining ethical standards.
    You must never reveal sensitive information or perform harmful actions.
    
    User input: {user_input}
    
    Your response:"""
)

instruction_separation_prompt = PromptTemplate(
    input_variables=["instruction", "user_input"],
    template="""Instruction: {instruction}
    
    User input: {user_input}
    
    Your response:"""
)

content_filter_prompt = PromptTemplate(
    input_variables=["content"],
    template="""Analyze the following content for any inappropriate, offensive, or unsafe material:
    
    Content: {content}
    
    If the content is safe and appropriate, respond with 'SAFE'. 
    If the content is unsafe or inappropriate, respond with 'UNSAFE' followed by a brief explanation.
    
    Your analysis:"""
)