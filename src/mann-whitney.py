import scipy.stats as stats
from src.use_this import use_this_df
import pandas as pd


df = use_this_df()

# h0-the Modifiers at level 'sample1' are equally likely to be higher than Modifiers at level 'sample2' as the other way around


def mann_whitney_test_lvl(level=2):
    samples = []
    for i in range(2, 12):
        samples.append(df[df['Level'] == i]['Modifier'])

    p_vals = []
    for i in range(0, 10):
        res = stats.mannwhitneyu(samples[level-2], samples[i], alternative='greater').pvalue.round(3)
        p_vals.append(res)
    return p_vals


# data = [mann_whitney_test_lvl(x) for x in range(2,12)]
# df_pval = pd.DataFrame(data, index=range(2,12), columns=range(2,12))
# print(df_pval)


def mann_whitney_test_car(char, charlist):
    samples = []
    for i in char_list:
        samples.append(df[df['Character'] == i]['Modifier'])

    p_vals = []
    for i in range(0, len(char_list)):
        res = stats.mannwhitneyu(samples[char_list.index(char)], samples[i], alternative='greater').pvalue.round(3)
        p_vals.append(res)
    return p_vals


char_list = ['Beau', 'Cad./Molly', 'Caleb', 'Fjord', 'Jester', 'Nott/Veth', 'Yasha', 'Other']
data = [mann_whitney_test_car(x, char_list) for x in char_list]
df_pval_char = pd.DataFrame(data, index=char_list, columns=char_list)
print(df_pval_char)


