import module as mo
import streamlit as st
import plotly.express as px

if __name__ == "__main__":
    df = mo.create_df()
    st_df = df.rename(columns={"Film": "Movie Name",
                            "Genre": "Movie Genre",
                            "Profitability": "Profitability in Millions $",
                            "Worldwide Gross": "Worldwide Gross in Millions $",
                            "Year": "Release Year"})

    st.title("Hollywood Movie Revenue")
    st.write("In this dashboard, we'll explore te revenue of Hollywood movies released from 2007-2011")
    st.header("Working Dataset")
    st.write("This is a quick glimpse into the dataset we will be using for this dashboard")
    st.dataframe(st_df, hide_index=True, height=500)