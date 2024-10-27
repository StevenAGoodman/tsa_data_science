import pandas as pd
import linecache

tid_key = []
with open("./data_gathering/title.basics.tsv", 'r', encoding="utf-8") as title_f:
    first = True
    for _, line in enumerate(title_f):
        if first:
            first = False
            continue
        line = line.split('\t')
        if line[1] == "movie":
            tid_key.append([line[0], line[2], line[7]])


# create tid key
data = []
with open("./data_gathering/title.ratings.tsv", encoding="utf-8") as ratings_f:
    first = True
    for line in ratings_f:
        if first:
            first = False
            continue
        line = line.split('\t')
        title, runtime = [(i[1], i[2]) for i in tid_key if line[0] in i]
        data.append([title, line[1], runtime])



        
df = pd.DataFrame(data)
df.set_index(0)
df.rename(columns={1:"title", 2:"avg_imdb_rating", 3:"runtime_min"})
df.to_csv("./data_gathering/imdb_ratings.csv")

