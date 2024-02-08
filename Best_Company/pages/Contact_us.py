import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv("topics.csv")
st.header("Contact Us")

with st.form(key = "Contact form"):

    user_email = st.text_input("Enter Your Email Address", placeholder = 'Username/Email')
    select = st.selectbox("What Topic do you want to Discuss with us", df["topic"], index = None, placeholder = 'Please choose the options')

    raw_message = st.text_area("Write Info Below", placeholder = 'Write here')

    message = f"""\
Subject: New email form {user_email}

from: {user_email}
Topic {select}
{raw_message}
"""

    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email, topic nd message was sent succeccfully!")