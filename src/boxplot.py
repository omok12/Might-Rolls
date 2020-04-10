from src.use_this import use_this_df
import seaborn as sns
import matplotlib.pyplot as plt


def plot_boxplot(df,x_col,y_col):
    sns.set_style('ticks')
    sns.color_palette('dark')
    ax = sns.boxplot(df[x_col], df[y_col])

    medians = df.groupby(x_col)[y_col].median().values
    nobs = df.groupby(x_col)[y_col].agg(['count'])
    nobs = ["n: " + str(i) for s in nobs.values for i in s]

    pos = range(len(nobs))
    for tick,label in zip(pos, ax.get_xticklabels()):
        ax.text(pos[tick], medians[tick] + 1, s=nobs[tick], horizontalalignment='center', size='x-small', color='w',
                weight='semibold')

    ax.set_title(f'{y_col} by {x_col} - Boxplot')

df = use_this_df()
plot_boxplot(df, 'Level','Modifier')
plt.show()
