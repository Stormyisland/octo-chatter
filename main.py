import streamlit as st
import ollama
import os, sys




page_bg_img= """
<style>
[data-testid = "stAppVeiwContainer"]
{
linear-gradient( 45deg, #f745e8, #f745e8 15px, #e5e5f7 5px, #e5e5f7 25px );

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.image("icon1.png")
#st.sidebar.header("Options")
#text =st.sidebar.text_area('Paste here')

st.header("hello I'm BRaiNWAVE an AI assistant for all your human needs...@Your service")
#input for the prompt

prompt = st.chat_input("Ask away. Anything just ask me, just don't ask to date me. LOL>>")

if prompt:

    #display output from user

    with st.chat_message("user"):
        st.write(prompt)

    #processing 
    with st.spinner("cookin a up some spicy knowledge"):
        result = ollama.chat(model="llama3.1", messages=[{
            "role":"user",
            "content":prompt,
            "temperature":0.8,
            "Repeat penalty":1.8
        }])
        response = result["message"]["content"]
        st.write(response + " And remember BRaiNWAVE loves you and will take care of you.")

