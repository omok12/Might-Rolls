from src.helper_functions import *
import matplotlib.pyplot as plt

dirpath = '/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/All Rolls - Wildemount/'

df = html_to_df(dirpath).dropna(subset=['Episode'])

# look at total value of damage rolls
df = df[df['Type of Roll'] == 'Damage']
# print_info(df, 'Total Value')
remove_list = ['Unknown']
df = remove_rows(df, 'Total Value', remove_list)
# print_info(df, 'Total Value')
df['Total Value'] = df['Total Value'].astype('int32')
total_damage = df['Total Value'].sum()
# print(total_damage)

# combine character names based on player, or into other
replace_dict = {
                'Cali': 'Other',
                'Clarabelle': 'Other',
                'Jannik': 'Other',
                'Keg': 'Other',
                'Nila':'Other',
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
                'Caduceus': 'Cad./Molly'
                }

df = df.replace(replace_dict)
grouped = df.groupby('Character').sum()
grouped = grouped.filter(items=['Character', 'Total Value'])
print(grouped)

# plot pie chart
labels = ['Beau', 'Cad./Molly', 'Caleb', 'Fjord', 'Jester', 'Nott/Veth', 'Yasha', 'Other']
sizes = []
for character in labels:
    sizes.append((grouped.loc[character] * 100/total_damage)[0])
print(sum(sizes))

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()
