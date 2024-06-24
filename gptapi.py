import os 
import openai
from openai import OpenAI

# Set environment variables
my_api_key = os.getenv('OPENAI_KEY')

openai.api_key = my_api_key


# WRITE YOUR CODE HERE