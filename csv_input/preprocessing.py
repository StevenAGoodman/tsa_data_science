import pandas as pd
import numpy as np

df = pd.read_csv("./csv_input/horror_movies.csv")

df.drop(columns={"original_title", "tagline", "poster_path", "adult", "backdrop_path", "collection","collection_name"})

df = df.loc[df["status"] != "In Production", :]

df.to_csv("./preprocessed_data.csv")