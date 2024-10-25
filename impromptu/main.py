import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# import data
data_df = pd.read_csv("./preprocessed_data.csv")

# config data in diff ways!
def config_data_tables(data_df):
  data_df

input_loc = sys.argv[1].replace("\\", "/")
print(input_loc)

def main(input_loc):

  input_df = pd.read_csv(input_loc)

  sns.pairplot(input_df, kind="reg")
  plt.show()


main(input_loc)
