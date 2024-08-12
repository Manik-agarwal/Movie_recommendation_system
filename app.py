from flask import Flask, request, jsonify
import joblib
import requests

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('movies.pkl')

TMDB_API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMjBmM2NhNGZhMjU5N2E3YmI3MmZlZjg3NTA5OGE0YSIsIm5iZiI6MTcyMzQ1OTk1My4xNDM1MzMsInN1YiI6IjY2YTUyODRjZTZjODU1YmZmZDM2NmJjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.n7onKGZ0WzDZ9BN0FxccIJng-yIL4a_AdIU_3J78QKo'

def get_movie_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    return None

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_title = data.get('title', '')
    
    # Generate recommendations
    recommendations = recommend(movie_title)
    
    # Fetch posters
    for movie in recommendations:
        movie['poster'] = get_movie_poster(movie['id'])
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
