import os 
import streamlit as st, langchain
from python_dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

st.title("Question Answering Chatbot")

with st.sidebar:
    st.title("Model Settings")
    api_key= st.text_input("Google API Key", value="your_api_key_here")
    model= st.text_input("Model", value="gemini-3.5-flash")
    temp=st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
    max_output_tokens=st.slider("Max Output Tokens", min_value=1, max_value=2048, value=1024, step=1)

llm = ChatGoogleGenerativeAI(
    api_key=api_key,
    model=model,
    temperature=temp,
    max_output_tokens=max_output_tokens
)

def get_user_input():
    user_input = st.text_input("Ask a question:")
    generate = st.button("Generate response")
    if generate:
        return user_input

def generate_response(user_input):
    response = llm.invoke(user_input)
    return response

user_input = get_user_input()

if user_input:
    response = generate_response(user_input)
    st.header("Response:")
    st.subheader(response.content[0]['text'])
