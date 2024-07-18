## movie_recommendation.py

from sklearn.neighbors import NearestNeighbors
import pandas as pd

class RecommendationSystem:
    def __init__(self, movie_data):
        self.movie_data = movie_data
        self.model = NearestNeighbors(n_neighbors=5, algorithm='auto')

    def train_model(self):
        movie_features = self.movie_data.pivot_table(index='movie_id', columns='user_id', values='rating').fillna(0)
        self.model.fit(movie_features)

    def get_personalized_recommendations(self, user_id):
        user_ratings = self.movie_data[self.movie_data['user_id'] == user_id]
        user_features = user_ratings.pivot_table(index='movie_id', columns='user_id', values='rating').fillna(0)
        distances, indices = self.model.kneighbors(user_features, n_neighbors=6)
        recommended_movies = []
        for i in range(1, len(distances.flatten())):
            recommended_movies.append(self.movie_data[self.movie_data['movie_id'] == indices.flatten()[i]]['movie_title'].values[0])
        return recommended_movies
