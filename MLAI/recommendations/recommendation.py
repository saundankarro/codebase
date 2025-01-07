import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore',category = FutureWarning)

ratings = pd.read_csv("data/ratings.csv")
print(f"Ratings DF Head:-")
print(ratings.head())

movies = pd.read_csv("data/movies.csv")
print("Movies DF Head:-")
print(movies.head())

n_ratings = len(ratings)
n_movies = len(ratings['movieId'].unique())
n_users = len(ratings['userId'].unique())

print(f"Number of ratings:- {n_ratings}")
print(f"Number of unique movieIDs:- {n_movies}")
print(f"Number of unique userz:- {n_users}")

print(f"Average rating per user:- {round(n_ratings/n_users, 2)}")
print(f"Average rating per movie:- {round(n_ratings/n_movies, 2)}")