import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

# Create a text element and let the reader know the data is loading.
st.sidebar.title('Sidebar')


@st.cache
def load_data():
    return sns.load_dataset('mpg')

mpg = load_data()

st.dataframe(mpg, width=1200)

# Sidebar Input
list_origins = mpg.origin.unique().tolist()
selected_origins = st.sidebar.multiselect('Country of Origin:', list_origins)

list_cylinders = mpg.cylinders.unique().tolist()
selected_cylinders = st.sidebar.multiselect('Number of Cylinders:', list_cylinders)

# Filters
filter_origins = list_origins if len(selected_origins) == 0 else selected_origins
filter_cylinders = list_cylinders if len(selected_cylinders) == 0 else selected_cylinders

# Prepare dataframe
f = (mpg.origin.isin(filter_origins) & mpg.cylinders.isin(filter_cylinders))
st.dataframe(mpg[f])

g = alt.Chart(mpg[f], width=700).mark_point().encode(
    x='weight',
    y='mpg'
)

st.altair_chart(g)