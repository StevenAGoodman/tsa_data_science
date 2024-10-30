import pandas as pd
import linecache

column_names = ["id", "format", "title", "old_title", "#", 'release_year', '#2', 'runtime', 'genre']
df = pd.DataFrame()

def imdb_og_filtering():
    with open("./data_gathering/imdb_processed_titles.tsv", 'r') as title_file:
        for line in title_file:
            line = line.split('\t')
            if line[1] == "movie" and "Horror" in line[8] or "Mystery" in line[8] or "Thriller" in line[8]:
                data = dict(map(lambda i,j : (i,j), column_names,line))
                data = pd.DataFrame(data, index=0)
                df = pd.concat([df, data], axis=0)

def imdb_titles_rating_merge():
    title_df = pd.read_csv("./data_gathering/imdb_processed_titles.tsv", sep="\t", names=["id", "format", "title", "old_title", "#", 'release_year', '#2', 'runtime', 'genre'])
    title_df.set_index("id", inplace=True)
    ratings_df = pd.read_csv("./data_gathering/title.ratings.tsv", sep="\t")
    ratings_df.set_index('tconst', inplace=True)
            
    df = pd.merge(title_df, ratings_df, left_index=True, right_index=True)
    df = df[["title","runtime","genre", "averageRating"]]
    df = df.set_index("title")
    return df

def main():
    imdb_df = imdb_titles_rating_merge()
    numbers_df = pd.read_csv("./data_gathering/theNumbers_finance.csv")
    numbers_df = numbers_df.set_index("title")[["release_date", "budget","global_revenue"]] 

    imdb_df = imdb_df[~imdb_df.index.duplicated(keep='first')]
    numbers_df = numbers_df[~numbers_df.index.duplicated(keep='first')]

    df = pd.concat([imdb_df, numbers_df], axis=1)
    df = df.loc[numbers_df.index]
    df.to_csv("./data_gathering/imdb_ratings.csv")
    
main()
