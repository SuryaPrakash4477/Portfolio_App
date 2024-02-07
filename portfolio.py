import streamlit as st

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/SuryaImage.jpg")

with col2:
    st.title("Surya Prakash Sharma")
    content = """
    Hi, I am Surya Prakash Sharma! I am a Python Programmer, Software Engineer-Embedded Team. I graduated in 2023 from Shoolini Unversity, Solan with 8.67 CGPA.
I am Working in Holmium Technology Comoany.
    """
    st.info(content)

st.write("Below you can find some of the apps I ahve Built in Pytho. Feel free to contact me")