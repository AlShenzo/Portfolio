import streamlit as st
from send_email import send_email
#from send_email file import send email_function

st.header('Contact Me')

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address ")# allow to enter one line of text
    message = st.text_area(label = "Your message", placeholder='Enter you message')# for multiline text
    message = f"""\
Subject: New email from {user_email}

from: {user_email}
{message}
"""
    button=st.form_submit_button('Submit')

    if button:
        send_email(message)
        st.info('Your email was sent')
      # essentially if pressed the button, the terminal will react and run.
      # button is actually a true / false, if we put print (button) above if button
      # and we dont press it it will say false
      # but if we pressed it and print(button) it will say true

