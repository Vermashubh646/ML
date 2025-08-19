import streamlit as st

# Set the title of the app
st.title("Hello, World!")

# Write a simple text
st.write("Welcome to your first Streamlit app.")

# Display a chart (example using random data)
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)
