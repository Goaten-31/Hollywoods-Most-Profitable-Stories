import module as mo
import streamlit as st
import plotly.express as px

if __name__ == "__main__":
    df = mo.create_df()

    st.title("Hollywood Movie Revenue")
    st.write("In this dashboard, we'll explore te revenue of Hollywood movies released from 2007-2011")