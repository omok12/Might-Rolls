from src.use_this import use_this_df
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = use_this_df()


ax = sns.boxplot(df['Level'], df['modifier'])

means = df.groupby('Level')['modifier'].mean().values
nobs = df.groupby('Level')['modifier'].agg(['count'])
nobs = ["n: " + str(i) for s in nobs.values for i in s]

pos = range(len(nobs))
for tick,label in zip(pos, ax.get_xticklabels()):
    ax.text(pos[tick], means[tick] + 1, s=nobs[tick], horizontalalignment='center', size='x-small', color='w',
            weight='semibold')
plt.show()
