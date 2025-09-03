'''
This script displays some graphics and buttons using Streamlit library.
This applications is launched on a web server (render.com) with the following link:

'''

import os
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image
import docx2txt
from PyPDF2 import PdfReader
import openpyxl

# Page configuration
img = Image.open("./images/image.png")
st.set_page_config(page_title="Streamlit: Example 2", layout="wide",
                   page_icon=img)


@st.cache_data
def load_image(img_file):
    return Image.open(img_file)


def read_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    count_page = len(pdf.pages)
    text = ""
    for i in range(count_page):
        page = pdf.pages[i]
        text += page.extract_text()
    return text


def save_file(file):
    # Create a directory for uploaded files if it doesn't exist
    os.makedirs("uploaded_files", exist_ok=True)
    with open(os.path.join("uploaded_files", file.name), "wb") as f:
        f.write(file.getbuffer())
    return st.success(f'File "{file.name}" saved in "uploaded_files" successfully!')


# Title
st.title("example2.py")

# Load Images------------------------------------------------------
st.header("Load Images", divider="gray")

image_file = st.file_uploader("Choose an image", type=["png", "jpeg", "jpg"])
if image_file is not None:
    st.image(load_image(image_file), width=500)
    # Save image in "uploaded_files"
    save_file(image_file)

# Load Excel or CSV files------------------------------------------
st.header("Load Excel or CSV files", divider="gray")

tabular_file = st.file_uploader(
    "Choose an Excel or CSV file", type=["xlsx", "csv"]
)

if tabular_file is not None:
    file_details = {"FileName": tabular_file.name,
                    "FileType": tabular_file.type, "FileSize": tabular_file.size}
    st.write(file_details)

    if tabular_file.type == "text/csv":
        df = pd.read_csv(tabular_file, sep='\t', header=0)

    elif tabular_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(tabular_file, engine='openpyxl', header=None)

    else:
        df = pd.DataFrame()

    st.dataframe(df, use_container_width=True)
    # Save image in "uploaded_files"
    save_file(tabular_file)

# Load PDF, Docx, txt files-----------------------------------------
st.header("Load PDF, Docx or txt files", divider="gray")

text_file = st.file_uploader(
    "Choose a PDF, Docx or txt file", type=["pdf", "docx", "txt"])
if text_file is not None:
    if text_file.type == "application/pdf":
        st.text_area("PDF Content", value=read_pdf(text_file), height=300)

    elif text_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        st.text_area("Docx Content", value=docx2txt.process(
            text_file), height=300)

    elif text_file.type == "text/plain":
        st.text_area("Txt Content", value=text_file.read().decode(
            "utf-8"), height=300)

    # Save text file in "uploaded_files"
    save_file(text_file)

# Inputs---------------------------------------------------------------
st.header("Inputs", divider="gray")
# Input one line
nombre = st.text_input("Name:")
st.write(nombre)

# Input multiple lines
mensaje = st.text_area("Message:", height=100)
st.write(mensaje)

# Input number
numero = st.number_input("Number:", 1, 25, step=1)
st.write(numero)

# Date
date = st.date_input("Date:")
st.write(date)

# Time
time = st.time_input("Time:")
st.write(time)

# Color
color = st.color_picker("Color:", "#056b05")
st.write(color)

# Image, video and audio------------------------------------------
# st.header("Image,Video & Audio", divider="gray")
# img = Image.open("./images/image.png")
# st.image(img, use_container_width=True, caption="Image 1")

# with open("./videos/video1.mp4", "rb") as video_file:
#     st.video(video_file.read(), start_time=0)

# with open("./videos/audio1.mp3", "rb") as audio_file:
#     st.audio(audio_file.read(), start_time=0)
