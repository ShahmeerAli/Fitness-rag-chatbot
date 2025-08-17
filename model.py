import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_tavily import TavilySearch 
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())


llm = ChatGroq(
    model="llama3-70b-8192",
    groq_api_key=os.environ.get("GROQ_API_KEY")
)


embeddings = HuggingFaceEmbeddings()
vector_store = FAISS.load_local("faiss_fitness_index", embeddings,allow_dangerous_deserialization=True)


retriever = vector_store.as_retriever(search_kwargs={'k': 3})

web_search=TavilySearch()


prompt = ChatPromptTemplate.from_template(
    """You are an Expert on Health and Fitness who answers every question. Answer the following question based on the provided context and if not present in the context you search for the answer:
    
    Context: {context}
    
    Question: {question}
    
    Answer:"""
)

def format_documents(docs):
    """Format retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)



def hybrid_search(question:str):
    fasi_docs=retriever.invoke(question)
    if fasi_docs:
        return "\n\n".join(doc.page_content for doc in fasi_docs)
    else:
     results= web_search.invoke(question)
     return "\n\n".join(res['content'] for res in results)


hybrid=RunnableLambda(hybrid_search)


rag_chain = (
    {"context": hybrid, "question": RunnablePassthrough()} 
    | prompt
    | llm
    | StrOutputParser()
)


query = "How to drink water in one second?"
print(rag_chain.invoke(query))

