import os
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


df=pd.read_csv("megaGymDataset.csv")

document=df.astype(str).agg(' '.join,axis=1).to_list()

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200
)

docs=text_splitter.create_documents(document)



embeddings=HuggingFaceEmbeddings()


vector_store=FAISS.from_documents(documents=docs,embedding=embeddings)
vector_store.save_local("faiss_fitness_index")


