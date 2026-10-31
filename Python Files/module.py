import pandas as pd
import numpy as np

def create_df():
    df = pd.read_csv("../Dataset/HollywoodsMostProfitableStories.csv")
    df = df.rename(columns={"Audience  score %" : "Audience Score %"})
    df = df.dropna()

    df = df.astype({"Audience Score %" : np.int8, "Rotten Tomatoes %" : np.int8, "Profitability" : np.float32, "Worldwide Gross" : np.float64})
    df["Profitability"], df["Worldwide Gross"] = np.round(df["Profitability"], 2), np.round(df["Worldwide Gross"], 2)
    return df

def name(df):
    list_of_items = set()
    df = df.sort_values(by='Lead Studio')
    for e in df['Lead Studio'].drop_duplicates():
        number_of_movies = len(df[df['Lead Studio'] == e])

        if number_of_movies > 1:
            list_of_items.add(f"{e}: {number_of_movies} Movies")
        else:
            list_of_items.add(f"{e}: {number_of_movies} Movie")
    return list_of_items