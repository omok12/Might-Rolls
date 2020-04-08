from src.helper_functions import *
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dirpath = '/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/All Rolls - Wildemount/'

# clean 'Natural Value' feature
df = html_to_df(dirpath).dropna(subset=['Episode'])
col = 'Natural Value'

# print_info(df, col)

d20_filter_out_list = ['Other', 'Damage', 'Fragment', 'Percentage', 'Unknown', 'Hit Dice']
df = remove_rows(df, 'Type of Roll', d20_filter_out_list)

# print_info(df, col)

remove_list = ['Unknown', 'Nat1', '-2', '24', '21', '0']
df = remove_rows(df, col, remove_list)

# print_info(df, col)


# plot histogram
data = df['Natural Value'].astype('int32')
sns.distplot(data,bins=np.arange(data.max()+2))
plt.show()