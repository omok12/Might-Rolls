import seaborn as sns
import numpy as np

def dist_plot(df, col):
    data = df[col]
    sns.distplot(data, bins=np.arange(data.min(), data.max()+1)).set_title(f'{col} Histogram')
