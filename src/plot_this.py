from src.helper_functions import *

def plot_this_df():
    # create df of level in each episode
    ep_formatted = pd.read_csv('/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/level_by_ep.csv', names=['episode_int','Episode','Level'])
    df_ep_level = ep_formatted.filter(['episode_int', 'Level']).set_index('episode_int')

    # fix episode names
    dirpath = '/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/All Rolls - Wildemount/'
    df = html_to_df(dirpath).dropna(subset=['Episode'])
    df['episode_int'] = df['Episode'].apply(lambda x: x[-2:]).astype('int64')

    # join df_epi_level
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
    df_filtered = df.filter(['Character', 'Type of Roll', 'Total Value', 'Natural Value', 'Notes', 'Level'])

    # cast value columns as int
    df_filtered['Total Value'] = df_filtered['Total Value'].astype('int32')
    df_filtered['Natural Value'] = df_filtered['Natural Value'].astype('int32')

    # create modifier column = total value - natural value
    df_filtered['modifier'] = df_filtered['Total Value'] - df_filtered['Natural Value']

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
