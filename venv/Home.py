import streamlit as st
import pandas

st.set_page_config(layout = 'wide')

col1, empty_col, col2 = st.columns([1.5, 0.7,1.5]) # create two columns to store in 2 objects
# we added an empty colum to make some space on the page
# we added and mention the dimension of it is ntead of the just 2 colums.

with col1:
    st.image("venv/image/photo.jpg")

with col2:
    st.title('Alan Shen')
    content = """ Hi, I am Alan! I'm a Python Programmer, Personal Trainer, I graduated from University of Surrey having studied Sport & Exercise Science,
    I have worked for various companies in the UK within the Fitness Industry, as a Personal Trainer, Health Advisor and Manager. 
    However I have found my passion in python programming. 
    I aim to keep learning and best myself in programming skills, also making world class web and graphic interface applications.
    """
    st.info(content)

content = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content)

col3, col4 = st.columns(2) # create two columns to store in 2 objects

df = pandas.read_csv('venv/data.csv', sep = ';') # this reads the CSV as a strcutred file and seperate them with ;

with col3:
    for index, row in df[:10].iterrows(): # with [:10] we split the rows and columns
        # ``iterrows`` returns a Series for each row,
        st.header(row["title"])
    # this created a header to write big text, write will do too
    # but header write H1 header

        st.write(row['description'])
        st.image('venv/image/' + row['image'])
        # we open the image file refer to he path of the folder
        # and we have the row['image'] to match image with the script filenames
        st.write(f"[Source Code]({row['url']})")
        # source code is the link name we want to display, and the link is the one next to it
        # to make it more dynamic we convert it into a f string, and curly bracket with the row['url']
        # whenever we change url the webpage will change the link accordingly

with col4:# with [10:] we split the rows and columns
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('venv/image/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

