from langchain-openai import OpenAI
from python import load_env

load_env()

llm = OpenAI(model_name="gpt-4")
response = llm.invoke("Who is Ashok Sharma In India Bihar ")
print(response)