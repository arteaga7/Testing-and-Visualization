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
import openpyxl
import datetime


def show_results():
    # Processed results ------------------------------------
    st.session_state.contador_testing = 1
    st.success('Testing performed successfully!')
    df = pd.read_excel("./data/processed/ABS_v1_report.xlsx",
                       engine='openpyxl', header=0)

    df = pd.read_excel("./data/processed/ABS_v1_report.xlsx",
                       engine='openpyxl', header=0)
    # To show a DataFrame with modification allowed
    df = st.data_editor(df)

    st.download_button(
        label="Download file",
        data=df.to_csv(sep='\t', index=False),
        file_name='report.csv'
    )

    color_map = {'Passed': 'green', 'Failed': 'red', 'Not_Applicable': 'gray'}
    fig_pie = px.pie(df, names='Verdict', color='Verdict',
                     title='Verdict Distribution', color_discrete_map=color_map)
    fig_pie.update_traces(textinfo='percent+value+label')
    st.plotly_chart(fig_pie, use_container_width=True)
    return


def testing_page():
    # Title
    st.title("Testing")

    # Load Excel file------------------------------------------
    st.header("Load FTS", divider="gray")

    if "contador_testing" not in st.session_state:
        st.session_state.contador_testing = 0

    fts_file = st.file_uploader(
        "Choose an Excel file", type=["xlsx"]
    )

    if fts_file is not None:
        df_fts = pd.read_excel(fts_file, engine='openpyxl', header=None)
        st.dataframe(df_fts, use_container_width=True)

        # Perform testing
        button_testing = st.button(label="Perform testing")

        if button_testing or st.session_state.contador_testing == 1:
            show_results()

    else:
        st.session_state.contador_testing = 0
    return


def show_metrics(df):
    st.subheader('Metrics for tested features')

    # Group by 'Feature' and obtain the total passed, failed, not applicable
    df_feature = df.groupby(
        'Feature')[['Passed', 'Failed', 'Not_Applicable']].sum()

    st.write(df_feature)

    color_map = {'Passed': 'green', 'Failed': 'red', 'Not_Applicable': 'gray'}
    fig_bar = px.bar(
        df_feature, title='Total TestCases by Feature', color_discrete_map=color_map)
    st.plotly_chart(fig_bar, use_container_width=True)
    return


def metrics_page():
    # Title
    st.title("Metrics")

    # Read DataFrame
    df = pd.read_csv(
        './data/processed/testing_results.csv', sep='\t', header=0)

    # Date
    date = (st.date_input("From date:", value=datetime.date(
        2025, 9, 1))).strftime('%d-%m-%Y')
    st.write(f"Filtered from date:")
    st.write(date)

    # Feature
    feature = ['All'] + list(df['Feature'].unique())

    feature_option = st.selectbox(
        label="Feature:",
        options=feature
    )
    st.write(f"Filtered by feature:")
    st.write(feature_option)

    if feature_option != 'All':
        df_metrics = df[(df['Date'] >= date) & (
            df['Feature'] == feature_option)]
    else:
        df_metrics = df[df['Date'] >= date]

    # DataFrame filtered
    st.write(df_metrics)
    show_metrics(df_metrics)
    return


# Page configuration ---------------------------------------------------
img = Image.open("./images/image.png")
st.set_page_config(page_title="HIL Component Tool", layout="wide",
                   page_icon=img)


# Sidebar --------------------------------------------------------------
st.sidebar.header("HIL Component Tool")

# Selectbox
selectbox_option = st.sidebar.selectbox(
    label="Select a page",
    options=['Testing', 'Metrics']
)

if selectbox_option == 'Testing':
    testing_page()
else:
    metrics_page()
# Sidebar --------------------------------------------------------------
