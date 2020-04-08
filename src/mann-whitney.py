import scipy.stats as stats
from src.use_this import use_this_df

df = use_this_df()

df_lvl_2 = df[df['Level'] == 2]
df_lvl_10 = df[df['Level'] == 10]

lvl_2_mod = df_lvl_2['modifier']
lvl_10_mod = df_lvl_10['modifier']

# h0 - the modifiers at level 10 are equally likely to be higher than modifiers at level 2 as the other way around

res = stats.mannwhitneyu(lvl_10_mod, lvl_2_mod, alternative='greater')
print(res.pvalue)
