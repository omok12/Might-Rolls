from src.use_this import use_this_df
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = use_this_df()

sns.set_style('ticks')
sns.color_palette('dark')
ax = sns.boxplot(df['Level'], df['Modifier'])

means = df.groupby('Level')['Modifier'].mean().values
nobs = df.groupby('Level')['Modifier'].agg(['count'])
nobs = ["n: " + str(i) for s in nobs.values for i in s]

pos = range(len(nobs))
for tick,label in zip(pos, ax.get_xticklabels()):
    ax.text(pos[tick], means[tick] + 1, s=nobs[tick], horizontalalignment='center', size='x-small', color='w',
            weight='semibold')
plt.show()
