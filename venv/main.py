import streamlit as st

st.set_page_config(layout = 'wide')

col1, col2 = st.columns(2)

with col1:
    st.image("venv/image/photo.jpg")

with col2:
    st.title('Alan Shen')
    content = """ Hi, I am Alan! I'm a Python Programmer, Personal Trainer, I graduated from University of Surrey having studied Sport & Exercise Science,
    I have worked for various companies in the UK within the Fitness Industry, as a Personal Trainer, Health Advisor and Manager. 
    However I have found my passion in programming and python. 
    I aim to keep learning and best myself in programming skills,
    and also making world class web and graphic interface applications.
    """
    st.info(content)

