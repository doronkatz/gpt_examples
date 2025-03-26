from typing import List
import os  # Import the os module for environment variable access
import openai  # Correct import for the OpenAI library
from dotenv import load_dotenv
import json

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_chatgpt(messages):
    response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content


prompt_role = """You are an assistant for journalists. 
Your task is to write articles, based on the FACTS that are given to you. 
You should respect the instructions: the TONE, the LENGTH, and the STYLE"""


def assist_journalist(facts: List[str], tone: str, length_words: int, style: str):
    facts = ", ".join(facts)
    prompt = f"{prompt_role}\nFACTS: {facts}\nTONE: {tone}\nLENGTH: {length_words} words\nSTYLE: {style}"
    return ask_chatgpt([{"role": "user", "content": prompt}])


print(
    assist_journalist(
        ["The sky is blue", "The grass is green"], "informal", 100, "blogpost"
    )
)
