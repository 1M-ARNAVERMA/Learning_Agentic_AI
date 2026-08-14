import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from environment
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file or environment variables.")

# Configure the API key
genai.configure(api_key=api_key)

# List out all available model names
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)
