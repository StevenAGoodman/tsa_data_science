import pandas as pd
import linecache

column_names = ["id", "format", "title", "old_title", "#", 'release_year', '#2', 'runtime', 'genre']
df = pd.DataFrame()

def type_filtering():
    with open("./data_gathering/imdb_processed_titles.tsv", 'r') as title_file:
        for line in title_file:
            line = line.split('\t')
            if line[1] == "movie" and "Horror" in line[8] or "Mystery" in line[8] or "Thriller" in line[8]:
                data = dict(map(lambda i,j : (i,j), column_names,line))
                data = pd.DataFrame(data, index=0)
                df = pd.concat([df, data], axis=0)

def main():
    title_df = pd.read_csv("./data_gathering/imdb_processed_titles.tsv", sep="\t")
    df.set_index(0, inplace=True)
    ratings_df = pd.read_csv("./data_gathering/title.ratings.tsv", sep="\t")
    df.set_index('tconst', inplace=True)
            
    df = pd.merge(title_df, ratings_df, left_index=True, right_index=True)
    df.set_index(0)
    df.rename(columns={1:"title", 2:"avg_imdb_rating", 3:"runtime_min"})
    df.to_csv("./data_gathering/imdb_ratings.csv")

