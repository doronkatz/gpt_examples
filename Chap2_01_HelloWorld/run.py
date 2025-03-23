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
    messages=[
        {
            "role": "system",
            "content": "You are a helpful teacher."
        },
        {
            "role": "user",
            "content": "Are there other measures that than time for complexity for an algorithm?"
        },
        {
            "role": "assistant",
            "content": "Yes there are other complexities besides time complexity for an algorithm, such as space complexity."
        },
        {
            "role": "user",
            "content": "What is it?"
        }
    ]
)

# Print the response
print(completion.choices[0].message.content)
