import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
There are some company employees who have working for the company more than 10 years
And they have good command in their specific feild and also mentioned their designation respectedly.
They getting good salary and perks too becuase of their skills and friendly nature.
"""
st.write(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data (2).csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])
