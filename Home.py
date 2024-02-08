import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

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

col3, col4 = st.columns(2)

df = pd.read_csv("data (1).csv", sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
        

