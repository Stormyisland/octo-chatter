import streamlit as st
import ollama
import os, sys




page_bg_img= """
<style>
[data-testid = "stAppVeiwContainer"]
{
linear-gradient( 45deg, #f745e8, #f745e8 5px, #e5e5f7 5px, #e5e5f7 25px );

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.image("icon1.png")
#st.sidebar.header("Options")
#text =st.sidebar.text_area('Paste here')

st.header("hello I'm BRaiNWAVE I am an AI assistant for all your needs...@Your service")
#input for the prompt

prompt = st.chat_input("Ask away. Anything just ask me, I'm so utterly interested>>")

if prompt:

    #display output from user

    with st.chat_message("user"):
        st.write(prompt)

    #processing 
    with st.spinner("Mind blowing knowledge on the way"):
        result = ollama.chat(model="llama3", messages=[{
            "role":"user",
            "content":prompt,
            "temperature":0.4,
            "Repeat penalty":1.6
        }])
        response = result["message"]["content"]
        st.write(response + " And always remember BRaiNWAVE AI loves you very much!")

