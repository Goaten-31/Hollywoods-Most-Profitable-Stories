import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def create_df():
    df = pd.read_csv("../Dataset/HollywoodsMostProfitableStories.csv")
    df = df.rename(columns={"Audience  score %" : "Audience Score %"})
    df = df.dropna()

    df = df.astype({"Audience Score %" : np.int8, "Rotten Tomatoes %" : np.int8, "Profitability" : np.float32, "Worldwide Gross" : np.float64})
    df["Profitability"], df["Worldwide Gross"] = np.round(df["Profitability"], 2), np.round(df["Worldwide Gross"], 2)
    return df

def numovies_perstdio(df):
    pass