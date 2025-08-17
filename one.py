import os
import pickle
import pandas as pd
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv,find_dotenv
_=load_dotenv(find_dotenv())



OPENAI_API_KEY=os.environ['GROQ_API_KEY']

llm=ChatGroq(
     model="llama3-70b-8192"   ,
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

prompt=ChatPromptTemplate.from_template(
    "tell me about {question}"
)

chain=prompt|llm|StrOutputParser()

response=chain.invoke({"question":"i am not in a good mood today. Tell me a joke"})
print(response)

