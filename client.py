import streamlit as st
import requests

def get_response_from_api(user_input):
    response = requests.post(
        "https://essay-generator-xx5k.onrender.com/essay/invoke",
        json={'input':{'topic':user_input}})
    

    return response.json()["output"]["content"]


st.title("Essay Generator")
input_text = st.text_input("Enter a topic for the essay:")

if st.button("Generate Essay"):
     st.write(get_response_from_api(input_text))