import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
import os

load_dotenv()

os.environ["LANGCHAIN_API"]=os.getenv("LANGCHAIN_API")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["OPENAI_API"] = os.getenv("OPENAI_API")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a good texting mate.Reply to the user in casual way and answer the queries."),
        ("user","question:{question}")
    ]
)

llm = Ollama(model='llama3')

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

st.title("Chatbot using llama-3 locally")
input = st.text_input("Ask anything!")

if st.button("submit"):
    st.write(chain.invoke({'question':input}))
