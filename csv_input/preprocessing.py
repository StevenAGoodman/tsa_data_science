import pandas as pd
import numpy as np
import os

#reset
try:
    os.remove('./preprocessed_data.csv')
except:
    print("preprocessed_data.csv nonexistent!")

data_loc = "./csv_input/horror_movies.xlsx"

# filtering
def filter_stuffs(df):
    print("filtering stuff...")
    df = df.drop(columns={"original_title", "tagline", "poster_path", "adult", "backdrop_path", "collection","collection_name"})
    df = df.loc[df["status"] != "In Production", :]
    df = df.loc[df["revenue"] > 100, :]
    df = df.loc[df["budget"] > 100, :]
    df = df.reset_index(drop=True)
    return df

# creating new columns
def operations(df):
    print("performing operations...")
    # spliting date into month / year / day
    year_col = []
    mo_col = []

    for val in df["release_date"].tolist():
        assert type(val) == "<class 'datetime.date'>" or "<class 'pandas._libs.tslibs.timestamps.Timestamp'>"
        year = val.year
        mo = val.month
        year_col.append(year)
        mo_col.append(mo)

    # getting profits
    profits_col = []
    for i in range(len(df)):
        revenue = df.iloc[i]["revenue"]
        costs = df.iloc[i]["budget"]
        profits = int(revenue) - int(costs)
        profits_col.append(profits)

    df = df.join(pd.DataFrame({"release_month":mo_col, "release_year":year_col, "profit":profits_col}))

    return df

def main(data_loc):
    print("loading data...")
    df = pd.read_excel(data_loc)

    df = filter_stuffs(df)
    df = operations(df)
    df = df.loc[df['profit'] > 50, :]
    df = df.reset_index(drop=True)

    print("result:")
    print(df)

    return df

df = main(data_loc)

df.to_csv("./preprocessed_data.csv")