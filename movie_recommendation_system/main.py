## main.py

from movie_recommendation import RecommendationSystem
from user_interface import app

if __name__ == "__main__":
    recommendation_system = RecommendationSystem()
    app.run()
