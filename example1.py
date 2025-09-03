'''
This script displays some graphics and buttons using Streamlit library.
This applications is launched on a web server (render.com) with the following link:

'''

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("./images/image.png")
st.set_page_config(page_title="Streamlit: Example 1", layout="centered",
                   page_icon=img, initial_sidebar_state="expanded")

# Read DataFrame
df = pd.read_csv('./data/dataframes.csv', sep='\t', header=0)

# Sidebar -----------------------------------------------
st.sidebar.header("Sidebar header")

# Slider
st.sidebar.subheader('Slider')
number_sidebar = st.sidebar.slider(
    key=1, label='Select a number', min_value=1, max_value=10,
    value=5  # Default value
)
st.sidebar.write(f'You selected number {number_sidebar}.')

# Select Slider
st.sidebar.subheader('Select Slider')
category_slider = st.sidebar.select_slider(
    key=2, label='Select a category',
    options=['Category 1', 'Category 2', 'Category 3'],
    value='Category 2'  # Default value
)
st.sidebar.write(f'Selected category: {category_slider}.')

# Checkbox
st.sidebar.header('Checkbox')
button_3 = st.sidebar.checkbox('Option 1')
button_4 = st.sidebar.checkbox('Option 2')

if button_3:
    st.sidebar.write('Option 1 selected.')
if button_4:
    st.sidebar.write('Option 2 selected.')

# Selectbox
st.sidebar.header('Selectbox')
selectbox_option = st.sidebar.selectbox(
    label="Select an option",
    options=['Option 1', 'Option 2', 'Option 3']
)
st.sidebar.write(f'Selected option: {selectbox_option}.')

# Radio
st.sidebar.header('Radio')
radio_option = st.sidebar.radio(
    label="Select an option",
    options=['Option 1', 'Option 2', 'Option 3']
)
st.sidebar.write(f'Selected option: {radio_option}.')

# --------------------------------------------------------
# Title
st.title("Main title")

# Markdown
st.markdown("### Markdown text.")

# Header
st.header("Header 1", divider="gray")

# Subheader
st.subheader("DataFrame")

# DataFrames
st.dataframe(df, use_container_width=True)
# Highlight the maximum value in each column
# st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
# To show a DataFrame (option 1)
# st.write(df.head(4))
# To show a DataFrame (option 2)
# st.table(df)
# To show a DataFrame with modification allowed
# df = st.data_editor(df)
st.write("To download any file, click the button below.")

st.download_button(
    label="Download file",
    data=df.to_csv(sep='\t', index=False),
    file_name='dataset.csv'
)

# Messages -------------------------------------------------------
st.header("Messages", divider="gray")

st.success('Success message built')
st.warning('Warning message built')
st.info('Info message built')
st.error('Error message built')
# st.exception('Exception message built')

# Code -------------------------------------------------------
st.header("Code", divider="gray")
st.code("print('Hello, World!')", language='python')
st.subheader('Json file')
st.json({"key": "value"})

# Plots with plotly.express as px and matplotlib.pyplot as plt---
st.header("Plots with plotly.express and matplotlib.pyplot", divider="gray")

st.subheader('Scatter plot')
# Scatter and bar plots do not have x_label and y_label
fig_scatter = px.scatter(df, x='Column1', y='Column3',
                         title='Column1 vs Column3')
# To display in the same window
st.plotly_chart(fig_scatter, use_container_width=True)
# To display in a new window
# fig_scatter.show()

fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(df['Column1'], df['Column3'], color='blue', alpha=0.5)
plt.title('Column1 vs Column3')
plt.xlabel('Column1')
plt.ylabel('Column3')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader('Bar plot')
# Scatter and bar plots do not have x_label and y_label
fig_bar = px.bar(df, x='Column3', y='Column2', title='Column3 vs Column2')
# To display in the same window
st.plotly_chart(fig_bar, use_container_width=True)

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(df['Column3'], df['Column2'], color='skyblue', alpha=0.5)
plt.title('Column3 vs Column2')
plt.xlabel('Column3')
plt.ylabel('Column2')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader('Line chart')
# line_chart does not have title
fig_line = st.line_chart(data=df, x='Column1', y='Column2', x_label='Index',
                         y_label='Values', color=None, width=70,
                         height=400, use_container_width=True)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(df['Column1'], df['Column2'], color='green', alpha=0.9)
plt.title('Column1 vs Column2')
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader('Histogram')
fig_histogram = px.histogram(df, x="Column3", title='Column3 vs count')
# To display in a new window
# fig_histogram.show()
# To display in the same window
st.plotly_chart(fig_histogram, use_container_width=True)

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(df['Column3'], bins=2, color='blue', alpha=0.8)
plt.title('Column3 vs count')
plt.xlabel('Column3')
plt.ylabel('count')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader('Pie chart')
fig_pie = px.pie(df, names='Column3', values='Column2',
                 title='Column3 vs Column2')
st.plotly_chart(fig_pie, use_container_width=True)

fig, ax = plt.subplots(figsize=(7, 4))
manzanas = [20, 10, 25, 30]
nombres = ["Ana", "Juan", "Diana", "Catalina"]
ax.pie(x=manzanas, labels=nombres, startangle=90, autopct='%1.1f%%')
plt.title('Column3 vs Column2')
st.pyplot(fig)

st.subheader('Boxplot')
fig, ax = plt.subplots(figsize=(7, 4))
ax.boxplot(df['Column1'], vert=True)
plt.title('Boxplot title')
plt.xlabel('Column1')
plt.ylabel('Values')
plt.xticks(rotation=0)
st.pyplot(fig)

# Divider ------------------------------------------------------
st.divider()

# Multiselector
st.header("Multiselect", divider="gray")
multiselect1 = st.multiselect(
    label="Select 1 column only",
    options=list(df.columns),
    max_selections=1,
)

# Button
button_hist = st.button(label="Display histogram and mean")
if button_hist:
    hist1 = px.histogram(df, x=multiselect1[0],
                         title=f'{multiselect1[0]} vs count',
                         )
    st.plotly_chart(hist1, use_container_width=True)
    mean1 = df[multiselect1[0]].mean()
    st.metric(label=f'Mean {multiselect1[0]}', value=f"{mean1:.2f}")
