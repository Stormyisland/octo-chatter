import streamlit as st
import ollama





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

st.header("hello I'm BRaiNWAVE your local AI assistaint...@Your service")
#input for the prompt

prompt = st.chat_input("Ask away.")

if prompt:

    #display output from user

    with st.chat_message("user"):
        st.write(prompt)

    #processing 
    with st.spinner("Tinkering and Thinkering"):
        result = ollama.chat(model="llama3", messages=[{
            "role":"assistant",
            "content":prompt,
        }])
        response = result["message"]["content"]
        st.write(response + " And always remember BRaiNWAVE loves you!")
