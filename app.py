import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved data
with open('movie_ls.pkl', 'rb') as f:
    movies = pickle.load(f)

with open('movie_sim.pkl', 'rb') as f:
    movie_similarity = pickle.load(f)

# Define recommend function
def recommend(selected_movie, movie_similarity, movies):
    # Get index of selected movie
    idx = movies.index[movies['MovieName'] == selected_movie][0]

    # Get similarity scores of all movies compared to selected movie
    sim_scores = list(enumerate(movie_similarity[idx]))

    # Sort movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 10 most similar movies
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    # Return recommended movie names and posters
    recommended_movie_names = list(movies.iloc[movie_indices]['MovieName'])
 
    return recommended_movie_names

# Define Streamlit app
st.title('Tamil Movie Recommender System')
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar - Movie selection
selected_movie = st.sidebar.selectbox('Select a movie:', movies['MovieName'].values)

# Main content
if st.button('Recommend'):
    # Get recommended movies
    recommended_movie_names = recommend(selected_movie, movie_similarity, movies)

    # Show recommended movies
    for i in range(len(recommended_movie_names)):
        st.subheader(recommended_movie_names[i])
        
