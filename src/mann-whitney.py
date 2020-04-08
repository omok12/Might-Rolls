import scipy.stats as stats
from src.use_this import use_this_df
import pandas as pd

df = use_this_df()

df_lvl_2 = df[df['Level'] == 2]
df_lvl_10 = df[df['Level'] == 10]

lvl_2_mod = df_lvl_2['modifier']
lvl_10_mod = df_lvl_10['modifier']

# h0-the modifiers at level 'sample1' are equally likely to be higher than modifiers at level 'sample2' as the other way around


def mann_whitney_test(sample1, sample2, i):
    res = stats.mannwhitneyu(sample1, sample2, alternative='greater').pvalue
    print(f"p-value for level{i+2} < level{i+3}: {res}")
    return res

samples = []
for i in range(2,12):
    samples.append(df[df['Level'] == i]['modifier'])

for i in range(0,9):
    mann_whitney_test(samples[i], samples[i+1], i)








