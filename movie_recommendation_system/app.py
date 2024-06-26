import requests
import streamlit as st
import pickle

movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = movies['title'].values

st.header('Movie Recommendation system')

selectvalue = st.selectbox("Select movie from dropdown",movies_list)


def fetch_image(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=4d3a1034d2d43cfcf71ead2901d17ad7".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x:x[1])
    recommended_movies = []
    recommended_poster = []
    for i in distance[1:6]:
        movies_id  = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_image(movies_id))
    return recommended_movies, recommended_poster


if st.button("Show recommendations"):
    movie_names,recommended_movies_poster = recommend(selectvalue)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(movie_names[1])   
        st.image(recommended_movies_poster[1])
    with col3:
        st.text(movie_names[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(movie_names[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(movie_names[4])
        st.image(recommended_movies_poster[4])
