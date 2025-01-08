import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore',category = FutureWarning)
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
def create_matrix(df):
    '''
    User-Item Matrix is a basic data structure in recommendation systems.

    Users and Movies are given indices, which then generate a matrix by the ratings corresponding to these indices.

    Input: Ratings Dataframe

    Output:
        user_mapper - Distinct User IDs are mapped to indexes
        movie_mapper - Distinct Movie IDs are mapped to indexes
        user_inv_mapper - Maps the indices in user_mapper back to User IDs
        movie_inv_mapper - Maps the indices in movie mapper back to Movie IDs
    '''
    N = len(df['userId'].unique())
    M = len(df['movieId'].unique())

    user_mapper = dict(zip(np.unique(df['userId']), list(range(N))))
    movie_mapper = dict(zip(np.unique(df['movieId']), list(range(M))))

    user_inv_mapper = dict(zip(list(range(N)), np.unique(df['userId'])))
    movie_inv_mapper = dict(zip(list(range(M)), np.unique(df['movieId'])))

    user_index = [user_mapper[i] for i in df['userId']]
    movie_index = [movie_mapper[i] for i in df['movieId']]

    X = csr_matrix((df['rating'], (movie_index, user_index)), shape := (M, N))

    return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper

def find_similar_movies(movie_id, X, k, metric = 'cosine', show_distance=False):

    neighbor_ids = []

    movie_ind = movie_mapper[movie_id]
    movie_vec = X[movie_ind]
    k+=1
    kNN = NearestNeighbors(n_neighbors=k, algorithm = "brute", metric=metric)
    kNN.fit(X)
    movie_vec = movie_vec.reshape(1,-1)
    neighbor = kNN.kneighbors(movie_vec, return_distance=show_distance)

    for i in range(0, k):
        n = neighbor.item(i)
        neighbor_ids.append(movie_inv_mapper[n])

    neighbor_ids.pop(0)
    return neighbor_ids

    

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

# Finding the highest and lowest rated movies

mean_ratings = ratings.groupby('movieId')[['rating']].mean()

lowest_rated = mean_ratings['rating'].idxmin()
movies.loc[movies['movieId']==lowest_rated]

highest_rated = mean_ratings['rating'].idxmax()
movies.loc[movies['movieId']==highest_rated]

# The number of people who rated movies the highest
ratings[ratings['movieId']==highest_rated]

# The number of people who rated movies the lowest
ratings[ratings['movieId']==lowest_rated]

movie_stats = ratings.groupby('movieId')[['rating']].agg(['count','mean'])
movie_stats.columns = movie_stats.columns.droplevel()

X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_matrix(ratings)

movie_titles = dict(zip(movies['movieId'], movies['title']))

movie_id = 3

similar_ids = find_similar_movies(movie_id, X, k=10)
movie_title = movie_titles[movie_id]

print(f"Since you have watched {movie_title}")
for i in similar_ids:
    print(movie_titles[i])