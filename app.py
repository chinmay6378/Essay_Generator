from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os   
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=0.1,
    huggingface_api_key=os.getenv("HuggingFaceHub_API_TOKEN")
)

model=ChatHuggingFace(llm=llm)

app = FastAPI()

prompt = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words."
)

add_routes(
    app,
    prompt | model,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
