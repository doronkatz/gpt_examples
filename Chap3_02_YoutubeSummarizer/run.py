import os  # Import the os module for environment variable access
import openai  # Correct import for the OpenAI library
from dotenv import load_dotenv
import json

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# Read the transcript from the file
with open("Chap3_02_YoutubeSummarizer/transcript.txt", "r") as f:
    transcript = f.read()

# Call the openai ChatCompletion endpoint, with the ChatGPT model
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user",
               "content": f"Summarize the following video transcript.: \n{transcript}"}])


print(response.choices[0].message.content)
