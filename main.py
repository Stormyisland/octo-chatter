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

st.header("hello I'm BRaiNWAVE your personal friendly AI...@Your service")
#input for the prompt

prompt = st.chat_input("Ask just about anything,come on try it. I have reasoning now!  >>")

if prompt:

    #display output from user

    with st.chat_message("user"):
        st.write(prompt)

    #processing 
    with st.spinner("Cooking up Super duper knowledge with Deepseek mega parameter AI, like huge actually massive, you don't even know"):
        result = ollama.chat(model="deepseek-r1:latest", messages=[{
            "role":"user",
            "content":prompt,
            "temperature":1.1
            ,
            "Repeat penalty":1.6
        }])
        response = result["message"]["content"]
        st.write(response + " And remember BRaiNWAVE says love one another and say no to war.")

