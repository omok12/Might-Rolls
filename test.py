from helper_functions import *
import matplotlib.pyplot as plt
import numpy as np

# create lists to clean data
dirpath = '/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/All Rolls - Wildemount/'
roll_type_out_list = ['Other', 'Damage', 'Fragment', 'Percentage', 'Unknown', 'Hit Dice']
nat_val_out_list = ['Unknown', 'Nat1', '-2', '24', '21', '0']
tot_val_out_list = ['Nat'+str(i) for i in range(21)]
tot_val_out_list.append('Unknown')

df = html_to_df(dirpath).dropna(subset=['Episode'])
df = remove_rows(df, 'Type of Roll', roll_type_out_list)
df = remove_rows(df, 'Natural Value', nat_val_out_list)
df = remove_rows(df, 'Total Value', tot_val_out_list)
df['Natural Value'] = df['Natural Value'].astype('int32')
df['Total Value'] = df['Total Value'].astype('int32')


# print(df['Natural Value'].astype('int32').describe())
# print(df['Total Value'].astype('int32').describe())

# plot stacked bar
ind = np.arange(6591)
nat_value = df['Natural Value']
total_value = df['Total Value']

p1 = plt.bar(ind, nat_value)
p2 = plt.bar(ind, total_value, bottom=nat_value)
plt.show()
