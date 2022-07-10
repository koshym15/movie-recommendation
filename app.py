import streamlit as st
import pandas as pd
import pickle
import requests
movies_list = pickle.load(open('movies_list2.pkl' , 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def poster(movie_id1):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=e8df1e86b53212b4574376bd1accfcf4&language=en-US".format(movie_id1)
     data = requests.get(url)
     data1 = data.json()
     poster_path = data1['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500" + poster_path
     return full_path


def recommend(movie):
     index = movies[movies['title_x'] == movie].index[0]
     distance = similarity[index]
     top5 = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
     recommendation =[]
     recommended_poster =[]
     for i in top5:
          movie_id = movies.iloc[i[0]].id
          recommendation.append((movies.iloc[i[0]].title_x))
          recommended_poster.append(poster(movie_id))
     return recommendation , recommended_poster

st.set_page_config(layout="wide")

st.title("Movie Recommendation system by Koshy")

# for form
select_movie_name = st.selectbox(
     'Enter your choice of movie',
     movies['title_x'].values)



#for button
if st.button('Recommend'):
     recommended_movies_name , recommended_movie_poster = recommend(select_movie_name)

     col1, col2 , col3 , col4 , col5 , col6 , col7 , col8 , col9 , col10 = st.columns([3,3, 3 , 3 , 3 ,3 ,3 ,3 ,3 ,3])
     with col1:
          st.text(recommended_movies_name[0])
          st.image(recommended_movie_poster[0])



     with col2:
          st.text(recommended_movies_name[1])
          st.image(recommended_movie_poster[1])


     with col3:
          st.text(recommended_movies_name[2])
          st.image(recommended_movie_poster[2])


     with col4:
          st.text(recommended_movies_name[3])
          st.image(recommended_movie_poster[3])

     with col5:
          st.text(recommended_movies_name[4])
          st.image(recommended_movie_poster[4])
     with col6:
          st.text(recommended_movies_name[5])
          st.image(recommended_movie_poster[5])
     with col7:
          st.text(recommended_movies_name[6])
          st.image(recommended_movie_poster[6])
     with col8:
          st.text(recommended_movies_name[7])
          st.image(recommended_movie_poster[7])

     with col9:
          st.text(recommended_movies_name[8])
          st.image(recommended_movie_poster[8])

     with col10:
          st.text(recommended_movies_name[9])
          st.image(recommended_movie_poster[9])



