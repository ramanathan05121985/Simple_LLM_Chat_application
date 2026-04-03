import streamlit as st
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


st.title("Simple LLM Chat Application")

with st.sidebar:
    st.title("Settings")
    api_key  = st.text_input("Enter the API Key:",type="password")

    #another method
    #api_key =st.secrets["OPENAI_API_KEY"]
    
if api_key:
    llm=ChatOpenAI(model="gpt-4.1-nano", max_completion_tokens=20,api_key=api_key)
    st.success("API key loaded successfully")
else:
    st.warning("Please enter your API key")

user_text=st.text_input("Please enter the query:")
if user_text:
    response=llm.invoke(user_text)
    st.success(response.content)

