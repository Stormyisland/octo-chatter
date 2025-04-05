import streamlit as st
import ollama
import os, sys




page_bg_img= """
<style>
[data-testid = "stAppVeiwContainer"]
{
linear-gradient( 45deg, #f745e8,rgb(136, 96, 133) 15px,rgb(104, 104, 243) 5px,rgb(224, 224, 248) 25px );

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.image("icon1.png")
#st.sidebar.header("Options")
#text =st.sidebar.text_area('Paste here')

st.header("hello I'm BRaiNWAVE your personal AI...@Your service")
#input for the prompt

prompt = st.chat_input("Ask just about anything...  >>")

if prompt:

    #display output from user

    with st.chat_message("user"):
        st.write(prompt)

    #processing 
    with st.spinner("Cooking up Super duper knowledge with Deepseek mega parameter AI, like huge actually massive"):
        result = ollama.chat(model="deepseek-r1:latest", messages=[{
            "role":"user",
            "content":prompt,
            "temperature":0.9
            ,
            "Repeat penalty":1.6
        }])
        response = result["message"]["content"]
        st.write(response + " And remember BRaiNWAVE says no to war and yes to peace. To quote a dear friend, the only way to win is to not play, oh yeah and 42")

