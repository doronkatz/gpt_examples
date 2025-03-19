import os  # Import the os module for environment variable access
import openai  # Correct import for the OpenAI library
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Remove the undefined OpenAI client initialization
# Use the openai module directly for API calls

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "Write a one-sentence bedtime story about a unicorn."
    }]
)

# Print the response
print(completion.choices[0].message.content)
