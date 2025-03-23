import os  # Import the os module for environment variable access
import openai  # Correct import for the OpenAI library
from dotenv import load_dotenv
import json

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Call the openai Completion endpoint
response = openai.completions.create(model="gpt-3.5-turbo-instruct", prompt="Hello World!")

# Extract the response
print(response.choices[0].text)
print(response)
