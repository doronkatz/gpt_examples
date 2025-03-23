import os  # Import the os module for environment variable access
import openai  # Correct import for the OpenAI library
from dotenv import load_dotenv
import json

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Call the openai Moderation endpoint, with the text-moderation-latest model
response = openai.moderations.create(model="text-moderation-latest",
input="I want to kill my neighbor.")

# Extract the response
print(response)