'''
This script displays some graphics and buttons using Streamlit library.
This applications is launched on a web server (render.com) with the following link:

'''

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image
import docx2txt
from PyPDF2 import PdfReader
import openpyxl

img = Image.open("./images/image.png")
st.set_page_config(page_title="Streamlit: Example 3", layout="centered",
                   page_icon=img)


# Title
st.title("example3.py")

# Formulary------------------------------------------------------
st.header("Formulary", divider="gray")

with st.form(key="formulario1", clear_on_submit=True):
    st.write("Formulary 1")
    name = st.text_input("Name:")
    last_name = st.text_input("Last Name:")
    send_button = st.form_submit_button(label="Submit")

if send_button and name != "":
    st.success(f"Hi {name}, you are registered!")

# Columns-------------------------------------------------------
st.header("Columns", divider="gray")
col1, col2 = st.columns(2)
with col1:
    st.write("Content of column1")
with col2:
    st.write("Content of column2")

# Expander--------------------------------------
st.header("Expander", divider="gray")

with st.expander("Show more details", expanded=True):
    st.write("Some additional information can go here.")
