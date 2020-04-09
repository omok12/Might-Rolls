from src.use_this import use_this_df
import seaborn as sns
import matplotlib.pyplot as plt


df = use_this_df()


def plot_distplots(df, col, col_wrap, plot_col):
    g = sns.FacetGrid(df, col=col, col_wrap=col_wrap)
    g.map(sns.distplot, plot_col)
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle(f'{plot_col} by {col}')

sns.set_style('ticks')

# plot_distplot(df, 'Character', 4, 'Total Value')
# plt.show()

# plot_distplot(df, 'Character', 4, 'Modifier')
# plt.show()

# plot_distplot(df, 'Level', 5, 'Total Value')
# plt.show()

plot_distplots(df, 'Level', 5, 'Modifier')
plt.show()

