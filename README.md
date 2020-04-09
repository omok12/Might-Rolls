# Mighty-Rolls
A dive into a Dungeons and Dragons 5e campaign


# Introduction

Dungeons and Dragons 5th edition (DnD 5e) is a tabletop role-playing game published by Wizards of the Coast
The core rules of the game are formed by three kind of d20(20-sided die) rolls; ability checks, attack rolls,
and saving throws.

Tasks in the game follow three steps:
1. Roll the die and add a modifier
2. Apply circumstantial bonuses and penalties
3. Compare the total to a target number

This presentation will focus on the modifier value added a die roll.


# Importing and Cleaning the Data

Dataset located [here](https://docs.google.com/spreadsheets/d/1FFuw5c6Hk1NUlHv2Wvr5b9AElLA51KtRl9ZruPU8r9k/edit#gid=0), as a Google Sheets spreadsheet, maintained by the [CritRoleStats](https://www.critrolestats.com/), includes 11107 rows and 11 columns.
After cleaning, there are 6591 rows, and 6 important columns;
‘Character’, ‘Type of Roll’, ‘Total Value’, ‘Natural Value’, ‘Level’, and ‘Modifier = (Total Value - Natural Value)’

<details>
  <summary>Import html to pandas DataFrame code</summary>
  
  ```
  def html_to_df(dirpath):
    frames = []
    for filename in os.listdir(dirpath):
        if filename.endswith('.html'):
            fullpath = os.path.join(dirpath, filename)
            frames.append(pd.read_html(fullpath, header=1, index_col=0)[0])
    return pd.concat(frames).reset_index(drop=True)
  ```
 </details>
 
 <details>
  <summary>Clean Dataframe code</summary>
  
  ```
    def remove_rows(df, col, lst):
        df = df[~df[col].isin(lst)]
        return df[df[col].notnull()]

    def use_this_df():
    # create df of level in each episode
    ep_formatted = pd.read_csv('/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/level_by_ep.csv', names=['episode_int','Episode','Level'])
    df_ep_level = ep_formatted.filter(['episode_int', 'Level']).set_index('episode_int')

    # fix episode names
    dirpath = '/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/All Rolls - Wildemount/'
    df = html_to_df(dirpath).dropna(subset=['Episode'])
    df['episode_int'] = df['Episode'].apply(lambda x: x[-2:]).astype('int64')

    # join df_ep_level
    df = df.join(df_ep_level, on='episode_int')

    # remove not d20 rolls
    d20_filter_out_list = ['Other', 'Damage', 'Fragment', 'Percentage', 'Unknown', 'Hit Dice']
    df = remove_rows(df, 'Type of Roll', d20_filter_out_list)

    # clean Total Value
    remove_list = ['Nat'+str(i) for i in range(21)]
    remove_list.append('Unknown')
    df = remove_rows(df, 'Total Value', remove_list)

    # clean Natural Value
    remove_list = ['Unknown', 'Nat1', '-2', '24', '21', '0']
    df = remove_rows(df, 'Natural Value', remove_list)

    # filter down df
    df_filtered = df.filter(['Character', 'Type of Roll', 'Total Value', 'Natural Value', 'Level'])

    # cast value columns as int
    df_filtered['Total Value'] = df_filtered['Total Value'].astype('int32')
    df_filtered['Natural Value'] = df_filtered['Natural Value'].astype('int32')

    # create modifier column = total value - natural value
    df_filtered['Modifier'] = df_filtered['Total Value'] - df_filtered['Natural Value']

    # merge characters
    replace_dict = {
        'Cali': 'Other',
        'Clarabelle': 'Other',
        'Jannik': 'Other',
        'Keg': 'Other',
        'Nila': 'Other',
        'Nott': 'Nott/Veth',
        'Molly': 'Cad./Molly',
        'Reani': 'Other',
        'Shakäste': 'Other',
        'Spurt': 'Other',
        'Summoned Creature': 'Other',
        'Twiggy': 'Other',
        'Veth': 'Nott/Veth',
        'Willi': 'Other',
        'Yarnball': 'Other',
        'Caduceus': 'Cad./Molly',
        'Beetles': 'Other',
        'Nugget': 'Other',
        'Duchess': 'Other',
        'Frumpkin': 'Other'
    }
    df_filtered = df_filtered.replace(replace_dict)
    return df_filtered
  ```
 </details>
