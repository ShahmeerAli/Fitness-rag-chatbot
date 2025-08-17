from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from model import rag_chain

app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class QuestionQuery(BaseModel):
    question:str


@app.post("/ask")
def ask_question(request:QuestionQuery):
    answer=rag_chain.invoke(request.question)
    return{"answer":answer}



