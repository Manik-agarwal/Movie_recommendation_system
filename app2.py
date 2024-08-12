import streamlit as st
import joblib
import requests

# Load the pre-trained model
model = joblib.load('movies.pkl')

# TMDb API key
TMDB_API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMjBmM2NhNGZhMjU5N2E3YmI3MmZlZjg3NTA5OGE0YSIsIm5iZiI6MTcyMzQ1OTk1My4xNDM1MzMsInN1YiI6IjY2YTUyODRjZTZjODU1YmZmZDM2NmJjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.n7onKGZ0WzDZ9BN0FxccIJng-yIL4a_AdIU_3J78QKo'

def get_movie_poster(movie_id):
    """Fetch the movie poster using TMDb API."""
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    return 'https://via.placeholder.com/200x300'

def recommend(movie):
    """Generate movie recommendations."""
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommendations = []
    for i in movies_list:
        movie_id = new_df.iloc[i[0]].movie_id  # Replace with actual movie ID column
        movie_title = new_df.iloc[i[0]].title
        recommendations.append({'title': movie_title, 'id': movie_id})
    
    return recommendations

def main():
    st.title("Movie Recommendation System")

    # Input field for the movie title
    user_input = st.text_input("Enter a movie title:")

    if user_input:
        st.write("Recommendations based on your input:")

        # Get recommendations
        recommendations = recommend(user_input)

        # Display recommendations
        for movie in recommendations:
            st.subheader(movie['title'])
            st.image(get_movie_poster(movie['id']), use_column_width=True)

if __name__ == "__main__":
    main()
