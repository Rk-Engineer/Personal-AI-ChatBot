import os
from dotenv import load_dotenv
import streamlit as st
from google import genai

# Load API key from .env (for local development)
load_dotenv()
api_key = os.getenv("API_KEY")

def ask(question):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"{question}"
    )
    return response.text

st.title("AI Chatbot", help="This is Rk's personalized Chatbot")
que = st.text_area("Enter the Query")

if st.button("Search") and que:
    answer = ask(que)
    st.markdown(answer)
