import os
import pandas as pd

# combine HTML tables in a dirpath into a concatenated dataframe
def html_to_df(dirpath):
    frames = []
    for filename in os.listdir(dirpath):
        if filename.endswith('.html'):
            fullpath = os.path.join(dirpath, filename)
            frames.append(pd.read_html(fullpath, header=1, index_col=0)[0])
    return pd.concat(frames).reset_index(drop=True)


# remove rows from a df based on a list and return notnull
def remove_rows(df, col, lst):
    df = df[~df[col].isin(lst)]
    return df[df[col].notnull()]


# print unique values and count of col
def print_info(df, col):
    print(df[col].unique())
    print(df[col].count())



