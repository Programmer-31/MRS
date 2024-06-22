import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    # Create a list of (index, distance) tuples and sort them
    movies_list_with_distances = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list_with_distances:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

# Load data from pickle files
movies_df = pd.read_pickle('movies.pkl')
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

option = st.selectbox("Select a movie to get recommendations:", movies_list)
st.write("You selected:", option)

if st.button("Recommend"):
    recommendations = recommend(option)
    st.write("Recommended movies:")
    for movie in recommendations:
        st.write(movie)

# streamlit run main.py