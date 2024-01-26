import streamlit as st
import pandas as pd

def space(n):
    for _ in range(n):
        st.write("")

def space_side(n):
    for _ in range(n):
        st.sidebar.write("")

@st.cache_data
def load_data(filename):
    data = pd.read_csv(filename)
    return data