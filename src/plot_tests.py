from src.plot_this import plot_this_df
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = plot_this_df()


# df_character = df[df['Character'] == 'Beau']
# df_character_level = df_character[df_character['Level'] == 2]
# print(df_character_level['Total Value'].count())
# sns.distplot(df_character['Total Value'])
# plt.show()



def plot_distplot(df, col, col_wrap, plot_col):
    g = sns.FacetGrid(df, col=col, col_wrap=col_wrap)
    g.map(sns.distplot, plot_col)


plot_distplot(df, 'Character', 4, 'Total Value')
plt.show()

# plot_distplot(df, 'Character', 4, 'modifier')
# plt.show()

# plot_distplot(df, 'Level', 6, 'Total Value')
# plt.show()

# plot_distplot(df, 'Level', 6, 'modifier')
# plt.show()

# sns.pairplot(df, hue="Character")
# plt.show()

# sns.boxplot(df['Character'], df['Total Value'])
# plt.show()