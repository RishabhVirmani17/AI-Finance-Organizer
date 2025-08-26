import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Check if the API key is loaded
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key found: {bool(api_key)}")
print(f"API Key value: {api_key[:10] if api_key else 'None'}...")

# Check the current directory and .env file
print(f"Current directory: {os.getcwd()}")
print(f".env file exists: {os.path.exists('.env')}")
