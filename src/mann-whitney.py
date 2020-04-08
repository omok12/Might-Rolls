import scipy.stats as stats
from src.use_this import use_this_df
import pandas as pd


df = use_this_df()

# h0-the modifiers at level 'sample1' are equally likely to be higher than modifiers at level 'sample2' as the other way around


def mann_whitney_test(level=2):
    samples = []
    for i in range(2, 12):
        samples.append(df[df['Level'] == i]['modifier'])

    p_vals = []
    for i in range(0, 10):
        res = stats.mannwhitneyu(samples[level-2], samples[i], alternative='greater').pvalue.round(3)
        p_vals.append(res)
    return p_vals


# samples = []
# for i in range(2, 12):
#     samples.append(df[df['Level'] == i]['modifier'])
# for i in range(0, 9):
#     res = stats.mannwhitneyu(samples[i], samples[i + 1], alternative='greater').pvalue
#     print(f"p-value for level{i + 2} < level{i + 3}: {res}")


data = [mann_whitney_test(x) for x in range(2,12)]
df_pval = pd.DataFrame(data, index=range(2,12), columns=range(2,12))
print(df_pval)
print(mann_whitney_test(2))





