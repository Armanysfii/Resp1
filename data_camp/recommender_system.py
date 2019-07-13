import pandas as pd
import numpy as np

metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

# mean rating across all movies
c = metadata['vote_average'].mean()

# number of votes received by a movie in the 90th percentile
m = metadata['vote_count'].quantile(0.90)

# filter movies that qualify for the chart, based on their vote counts
# Filter out all qualified movies into a new DataFrame
q_movies = metadata.copy().loc[metadata['vote_count'] >= m]


# calculate your metric for each qualified movie

# Function that computes the weighted rating of each movie
def weighted_rating(x, m=m, c=c):
    v = x['vote_count']
    r = x['vote_average']
    # calculation based on the IMDB formula
    return (v / (v + m) * r) + (m / (m + v) * c)


q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

# print(q_movies.iloc[0])

# sort movies based on score calculated above
q_movies = q_movies.sort_values('score', ascending=False)

# the top 10 movies
# print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10))


 ### CONTENT BASED RECOMMENDER SYSTEM ###

# print(metadata['overview'].head())

from sklearn.feature_extraction.text import TfidfVectorizer

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

# replace NaN with an empty string
metadata['overview'] = metadata['overview'].fillna('')

# construnct the required tfidf matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(metadata['overview'])

# 75k different word were used to describe the 45k movies in the dataset
# print(tfidf_matrix.shape)


 ### similarity score ###

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# construct a reverse map of indices and movie titles
indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

