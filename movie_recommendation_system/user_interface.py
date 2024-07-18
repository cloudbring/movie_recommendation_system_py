## user_interface.py

from flask import Flask, request
from movie_recommendation import RecommendationSystem

app = Flask(__name__)
recommendation_system = RecommendationSystem()  # Set default value

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    user_id = request.args.get('user_id')  # Get user_id from request
    if user_id:
        recommendations = recommendation_system.get_personalized_recommendations(user_id)  # Get personalized recommendations
        return {'recommendations': recommendations}, 200  # Return recommendations with status code 200
    else:
        return {'error': 'User ID is required'}, 400  # Return error message with status code 400 if user_id is not provided
