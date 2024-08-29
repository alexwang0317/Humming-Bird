from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Check if the environment variable is loaded correctly
openai_api_key = os.getenv("OPENAI_API_KEY")

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert programmer, especially capable at writing code using MavSDK.",
        ),
        ("human", "{text}"),
    ]
)
_model = ChatOpenAI(openai_api_key=openai_api_key)

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model


