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
  <summary>Import code</summary>
  
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

