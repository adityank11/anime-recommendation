import streamlit as st
from mal import Anime
import pickle

st.set_page_config(layout="wide")

def fetch_poster(anime_id):
    poster_link = Anime(mal_id=anime_id).image_url
    return poster_link


def recommend(anime):
    index = animes[animes['Name'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_anime_names = []
    recommended_anime_posters = []
    for i in distances[1:6]:
        # fetch the anime poster
        anime_id = animes.iloc[i[0]].MAL_ID
        recommended_anime_posters.append(fetch_poster(anime_id))
        recommended_anime_names.append(animes.iloc[i[0]].Name)
    return recommended_anime_names,recommended_anime_posters


st.title('Anime Recommendation System')
animes = pickle.load(open('anime_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
anime_list = animes['Name'].values
selected_anime = st.selectbox("Type or select an anime from the dropdown",anime_list)



if st.button('Show Recommendation'):
    recommended_anime_names,recommended_anime_posters = recommend(selected_anime)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_anime_names[0])
        st.image(recommended_anime_posters[0])
    with col2:
        st.text(recommended_anime_names[1])
        st.image(recommended_anime_posters[1])
    with col3:
        st.text(recommended_anime_names[2])
        st.image(recommended_anime_posters[2])
    with col4:
        st.text(recommended_anime_names[3])
        st.image(recommended_anime_posters[3])
    with col5:
        st.text(recommended_anime_names[4])
        st.image(recommended_anime_posters[4])