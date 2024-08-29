from .chain import chain

__all__ = ["chain"]

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Check if the environment variable is loaded correctly
openai_api_key = os.getenv("OPENAI_API_KEY")
