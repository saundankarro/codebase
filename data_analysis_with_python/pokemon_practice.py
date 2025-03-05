import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Download latest version
# path = kagglehub.dataset_download("navtiw/pokemon")

# print("Path to dataset files:", path)

pokedf = pd.read_csv('data/pokemon.csv')

# Get information on dataset
print(pokedf.head())

print(pokedf.info())

# Removing extra columns
pokedf = pokedf.drop(columns=['img_url','version_x','version_y'])


# Cleaning the columns
cols = ['gender','type','weakness']
pokedf[cols] = pokedf[cols].apply(lambda x: x.str.strip())

# Adding generations

pokedf['generation'] = np.select([
    (pokedf.id >= 1) & (pokedf.id <= 151),
    (pokedf.id >= 152) & (pokedf.id <= 251),
    (pokedf.id >= 252) & (pokedf.id <= 386),
    (pokedf.id >= 387) & (pokedf.id <= 493),
    (pokedf.id >= 494) & (pokedf.id <= 649),
    (pokedf.id >= 650) & (pokedf.id <= 721),
    (pokedf.id >= 722) & (pokedf.id <= 809),
    (pokedf.id >= 810) & (pokedf.id <= 905),
    (pokedf.id >= 906) & (pokedf.id <= 1025)
],
[
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
],
"unknown generation")

print(pokedf.head())

print(pokedf.info())


'''
Creating a plot to show the count of Pokemon in each type to understand the spread of Pokemon types. 
As a Pokemon can have one type (i.e. Pikachu is only Electric type) or two types (i.e. Charizard is Fire and Flying),
I exploded the dataframe in order to ensure that two-typed Pokemon are counted for each type.

By exploding the dataset, I am able to ensure that the two-typed Pokemon can be counted for both their typings. This means
that Charizard will be included in both the Fire type Pokemon count and the Flying type Pokemon count.
'''
typedf = pokedf.assign(type=pokedf['type'].str.split(',')).explode('type')
typedf[cols] = typedf[cols].apply(lambda x: x.str.strip())
print(f"typedf:- {typedf.head(20)}")

cnt_types = typedf["type"].value_counts()

print(f"cnt_types:- {cnt_types.head(20)}")

plt.bar(cnt_types.index, cnt_types.values)
plt.show()


'''
The following code creates 2 sets of pie graphs that highlights the number of pokemon types spread out by generation. The 
first set highlights the spread of pokemon types in each generation, while the second set highlights the count of each type
in the generations. This is to highlight the spread of types per generation to get a better understanding of how the pokemon 
are distributed throughout the generations and pokemon world.
'''

# First set of pie graphs
gendf = pokedf.assign(type=pokedf['type'].str.split(',')).explode('type')
gendf[cols] = gendf[cols].apply(lambda x: x.str.strip())

gen_types = gendf.groupby('generation', as_index=False)['type'].value_counts()

print(f"gen_types:- \n{gen_types.head(20)}")

gen_types = gen_types.astype({'generation':'object','count': 'Int64'})

gen_types = gen_types.pivot(index='type',columns='generation', values='count')

print(f"gen_types column types :- \n {gen_types.dtypes}")
gen_types.plot.pie(subplots=True ,legend=False, layout=(3,3))


# Second set of pie graphs
types_gen = gendf.groupby('generation', as_index=False)['type'].value_counts()

print(f"types_gen:- \n{types_gen.head(20)}")

types_gen = types_gen.astype({'generation':'object','count': 'Int64'})

types_gen = types_gen.pivot(index='generation',columns='type', values='count')

print(f"types_gen column types :- \n {types_gen.dtypes}")
types_gen.plot.pie(subplots=True ,legend=False, layout=(5,5))


'''
Creating a plot to show the count of Pokemon type weaknesses. By looking at the spread of Pokemon types as weaknesses,
I can understand what types can have the greatest spread of strength against other Pokemon. For example, if 40 Pokemon have
weakness to fire and 60 Pokemon have weakness to water, I can understand that more Pokemon are weaker against water than fire.

By exploring the Pokemon type weaknesses, I can understand what Pokemon types are more likely to have an effective fight against
an unknown team of Pokemon
'''

weakdf = pokedf.assign(weakness=pokedf['weakness'].str.split(r',')).explode('weakness')
weakdf[cols] = weakdf[cols].apply(lambda x: x.str.strip())
print(weakdf.head(25))

weakdf = weakdf.drop(weakdf[weakdf.weakness == ''].index)
print(weakdf.describe())

a = weakdf['weakness'].unique()
print(f"Sorted list:- {sorted(a)}")

weak_types = weakdf['type'].value_counts()

print(f"weak_types:- \n{weak_types.head(20)}")

plt.bar(weak_types.index, weak_types.values)
plt.show()