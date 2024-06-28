import streamlit as st
import pandas as pd
import pickle
import requests
import random


st.set_page_config(page_title="Movie Recommendation System", page_icon=":wave:")
st.sidebar.header("Welcome")

all_data = pickle.load(open("data/alldata.pkl", "rb"))
movies = pickle.load(open("data/movie_list.pkl", "rb"))
similarity = pickle.load(open("data/similarity.pkl", "rb"))
genre = pickle.load(open("data/finalgenre.pkl", "rb"))
movie_list = movies["title"].values
genre_list = genre["new_genre"].values

tabs = [
    "Categories",
    "Movie Recommend",
    "Random Movie",
    "Show Top Movies",
]
st.sidebar.header("Choose What You Looking For:")
selected_tab = st.sidebar.selectbox("Choices : ", tabs)

st.sidebar.markdown(
    """
---
`Created by Ömer Bilen` 
"""
)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(
        movie_id
    )
    data = requests.get(url)
    data = data.json()
    if "poster_path" in data:
        poster_path = data["poster_path"]
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return "https://i.ibb.co/8DJ1z0t/default-poster.jpg"


if selected_tab == "Movie Recommend":
    st.markdown(
        "<h1 style='text-align:center;'>Movie Recommendation System</h1>",
        unsafe_allow_html=True,
    )
    select_value = st.selectbox("Select Movie", movie_list)

    def recommend(movie_name):
        index = movies[movies["title"] == movie_name].index[0]
        distance = sorted(
            list(enumerate(similarity[index])),
            reverse=True,
            key=lambda vector: vector[1],
        )
        recommend_movie = []
        recommend_poster = []
        for i in distance[1:7]:
            movies_id = movies.iloc[i[0]].movie_id
            recommend_movie.append(movies.iloc[i[0]].title)
            recommend_poster.append(fetch_poster(movies_id))
        return recommend_movie, recommend_poster

    if st.button("Show Recommended Movies"):
        selected_movie, movie_poster = recommend(select_value)
        selected_movie_id = movies[movies["title"] == select_value].iloc[0].movie_id
        selected_movie_genre = movies[movies["title"] == select_value].iloc[0].genre
        selected_movie_overview = (
            movies[movies["title"] == select_value].iloc[0].overview
        )
        selected_movie_language = (
            movies[movies["title"] == select_value].iloc[0].original_language
        )
        selected_movie_release_date = (
            movies[movies["title"] == select_value].iloc[0].release_date
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"<h3>{select_value}</h3>"
                f"<p><strong>Category :</strong> {selected_movie_genre}</p>"
                f"<p><strong>Release Date:</strong> {selected_movie_release_date}</p>"
                f"<p><strong>Original Language :</strong> {selected_movie_language}</p>",
                unsafe_allow_html=True,
            )
            with st.expander("Click to read overview"):
                st.write(f"Overview: {selected_movie_overview}")

        with col2:
            st.image(fetch_poster(selected_movie_id), width=300)

        st.write("\n")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("\n")

        col3, col4, col5 = st.columns(3)

        with col3:
            st.markdown(f"<b>{selected_movie[0]}</b>", unsafe_allow_html=True)
            st.image(movie_poster[0], width=300)
            with st.expander("Click to read overview"):
                st.markdown(
                    f"<h3>{selected_movie[0]}</h3>"
                    f"<p><strong>Category :</strong> {movies[movies['title'] == selected_movie[0]].iloc[0].genre}</p>"
                    f"<p><strong>Release Date:</strong> {movies[movies['title'] == selected_movie[0]].iloc[0].release_date}</p>"
                    f"<p><strong>Original Language :</strong> {movies[movies['title'] == selected_movie[0]].iloc[0].original_language}</p>",
                    unsafe_allow_html=True,
                )
                st.write(
                    f"Overview: {movies[movies['title'] == selected_movie[0]].iloc[0].overview}"
                )

        with col4:
            st.markdown(f"<b>{selected_movie[1]}</b>", unsafe_allow_html=True)
            st.image(movie_poster[1], width=300)
            with st.expander("Click to read overview"):
                st.markdown(
                    f"<h3>{selected_movie[1]}</h3>"
                    f"<p><strong>Category :</strong> {movies[movies['title'] == selected_movie[1]].iloc[0].genre}</p>"
                    f"<p><strong>Release Date:</strong> {movies[movies['title'] == selected_movie[1]].iloc[0].release_date}</p>"
                    f"<p><strong>Original Language :</strong> {movies[movies['title'] == selected_movie[1]].iloc[0].original_language}</p>",
                    unsafe_allow_html=True,
                )
                st.write(
                    f"Overview: {movies[movies['title'] == selected_movie[1]].iloc[0].overview}"
                )

        with col5:
            st.markdown(f"<b>{selected_movie[2]}</b>", unsafe_allow_html=True)
            st.image(movie_poster[2], width=300)
            with st.expander("Click to read overview"):
                st.markdown(
                    f"<h3>{selected_movie[2]}</h3>"
                    f"<p><strong>Category :</strong> {movies[movies['title'] == selected_movie[2]].iloc[0].genre}</p>"
                    f"<p><strong>Release Date:</strong> {movies[movies['title'] == selected_movie[2]].iloc[0].release_date}</p>"
                    f"<p><strong>Original Language :</strong> {movies[movies['title'] == selected_movie[2]].iloc[0].original_language}</p>",
                    unsafe_allow_html=True,
                )
                st.write(
                    f"Overview: {movies[movies['title'] == selected_movie[2]].iloc[0].overview}"
                )

        st.write("\n")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("\n")

        col6, col7, col8 = st.columns(3)
        with col6:
            st.markdown(f"<b>{selected_movie[3]}</b>", unsafe_allow_html=True)
            st.image(movie_poster[3], width=300)
            with st.expander("Click to read overview"):
                st.markdown(
                    f"<h3>{selected_movie[3]}</h3>"
                    f"<p><strong>Category :</strong> {movies[movies['title'] == selected_movie[3]].iloc[0].genre}</p>"
                    f"<p><strong>Release Date:</strong> {movies[movies['title'] == selected_movie[3]].iloc[0].release_date}</p>"
                    f"<p><strong>Original Language :</strong> {movies[movies['title'] == selected_movie[3]].iloc[0].original_language}</p>",
                    unsafe_allow_html=True,
                )
                st.write(
                    f"Overview: {movies[movies['title'] == selected_movie[3]].iloc[0].overview}"
                )

        with col7:
            st.markdown(f"<b>{selected_movie[4]}</b>", unsafe_allow_html=True)
            st.image(movie_poster[4], width=300)
            with st.expander("Click to read overview"):
                st.markdown(
                    f"<h3>{selected_movie[4]}</h3>"
                    f"<p><strong>Category :</strong> {movies[movies['title'] == selected_movie[4]].iloc[0].genre}</p>"
                    f"<p><strong>Release Date:</strong> {movies[movies['title'] == selected_movie[4]].iloc[0].release_date}</p>"
                    f"<p><strong>Original Language :</strong> {movies[movies['title'] == selected_movie[4]].iloc[0].original_language}</p>",
                    unsafe_allow_html=True,
                )
                st.write(
                    f"Overview: {movies[movies['title'] == selected_movie[4]].iloc[0].overview}"
                )

        with col8:
            st.markdown(f"<b>{selected_movie[5]}</b>", unsafe_allow_html=True)
            st.image(movie_poster[5], width=300)
            with st.expander("Click to read overview"):
                st.markdown(
                    f"<h3>{selected_movie[5]}</h3>"
                    f"<p><strong>Category :</strong> {movies[movies['title'] == selected_movie[5]].iloc[0].genre}</p>"
                    f"<p><strong>Release Date:</strong> {movies[movies['title'] == selected_movie[5]].iloc[0].release_date}</p>"
                    f"<p><strong>Original Language :</strong> {movies[movies['title'] == selected_movie[5]].iloc[0].original_language}</p>",
                    unsafe_allow_html=True,
                )
                st.write(
                    f"Overview: {movies[movies['title'] == selected_movie[5]].iloc[0].overview}"
                )

elif selected_tab == "Categories":
    st.markdown(
        "<h1 style='text-align:center;'>Movie Categories</h1>",
        unsafe_allow_html=True,
    )
    Categories = [
        "Action",
        "Adventure",
        "Animation",
        "Comedy",
        "Crime",
        "Drama",
        "Family",
        "Fantasy",
        "History",
        "Mystery",
        "Romance",
        "War",
        "Thriller",
        "Western",
        "Science Fiction",
        "Music",
        "TV Movie",
        "Horror",
    ]
    Categories.sort()
    select_genre = st.multiselect("Select Categories", Categories)

    if st.button("Show Random Movie in Selected Categories"):
        selected_genre_movies = genre[genre["new_genre"].isin(select_genre)]

        if not selected_genre_movies.empty:
            matching_movie_ids = (
                selected_genre_movies.groupby("movie_id")
                .filter(lambda x: len(x) == len(select_genre))["movie_id"]
                .unique()
            )

            if len(matching_movie_ids) > 0:
                random_selected_movie_id = random.choice(matching_movie_ids)
                random_selected_movie = movies[
                    movies["movie_id"] == random_selected_movie_id
                ]
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(
                        f"<h3>Movie Name : {random_selected_movie['title'].values[0]}</h3>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f"<big>Release Date : {random_selected_movie['release_date'].values[0]}</big>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f"<big>Original Language : {random_selected_movie['original_language'].values[0]}</big>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f"<big>Overview : {random_selected_movie['overview'].values[0]}</big>",
                        unsafe_allow_html=True,
                    )
                with col2:
                    random_selected_movie_poster = fetch_poster(
                        random_selected_movie_id
                    )
                    st.image(
                        random_selected_movie_poster,
                        width=350,
                    )
            else:
                st.warning("No movies found with all the selected genres.")
        else:
            st.warning("No movies found in the selected categories.")

elif selected_tab == "Random Movie":
    st.markdown(
        "<h1 style='text-align:center;'>Random Movie</h1>",
        unsafe_allow_html=True,
    )
    button = st.button("Give Me a Movie")

    col1, col2 = st.columns(2)

    if button:
        with col1:
            random_movie = random.choice(movie_list)
            movie_info = movies[movies["title"] == random_movie].iloc[0]

            st.markdown(
                f"<h3>{random_movie}</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<big>Category : {movie_info['genre']}</big>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<big>Release Date : {movie_info['release_date']}</big>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<big>Original Language : {movie_info['original_language']}</big>",
                unsafe_allow_html=True,
            )
            with st.expander("Click to read overview"):
                st.write(f"Overview: {movie_info['overview']}")

        with col2:
            random_movie_id = movies[movies["title"] == random_movie].iloc[0].movie_id
            random_movie_poster = fetch_poster(random_movie_id)
            st.image(
                random_movie_poster,
                width=350,
            )

elif selected_tab == "Show Top Movies":
    st.markdown(
        "<h1 style='text-align:center;'>Top Movies</h1>",
        unsafe_allow_html=True,
    )
    V = all_data["vote_count"]
    R = all_data["vote_average"]
    C = all_data["vote_average"].mean()
    m = all_data["vote_count"].quantile(0.75)

    all_data["weighted_average"] = (V / (V + m) * R) + (m / (m + V) * C)
    all_data = all_data.sort_values(by="weighted_average", ascending=False)
    selected_columns = [
        "title",
        "release_date",
        "genre",
        "original_language",
        "movie_id",
    ]
    column_mapping = {
        "title": "Movie's Name",
        "release_date": "Release Date",
        "genre": "Genre ",
        "original_language": "Original Language",
    }

    tabs3 = ["Top 10 Movies", "Top 20 Movies", "Top 50 Movies", "Top 99 Movies"]
    selected_top = st.selectbox("Choose Top List : ", tabs3)

    if selected_top == "Top 10 Movies":
        top_10_movies = all_data[selected_columns].head(10)

        movie_info_list = []
        for index, movie in top_10_movies.iterrows():
            movie_info = {
                "Name": movie["title"],
                "PosterURL": fetch_poster(movie["movie_id"]),
            }
            movie_info_list.append(movie_info)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("\n")

        columns = st.columns(3)
        for i, movie_info in enumerate(movie_info_list):
            with columns[i % 3]:
                st.markdown(
                    f"""
                <div style='display: grid; place-items: center;'>
                    <strong>{movie_info['Name']}</strong>
                    <img src="{movie_info['PosterURL']}" width="250"/>
                </div>
                """,
                    unsafe_allow_html=True,
                )
                st.write("\n")
                st.write("\n")
                st.write("\n")

        st.table(all_data[selected_columns].head(10).rename(columns=column_mapping))

    elif selected_top == "Top 20 Movies":
        top_20_movies = all_data[selected_columns].head(20)

        movie_info_list = []
        for index, movie in top_20_movies.iterrows():
            movie_info = {
                "Name": movie["title"],
                "PosterURL": fetch_poster(movie["movie_id"]),
            }
            movie_info_list.append(movie_info)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("\n")

        columns = st.columns(3)
        for i, movie_info in enumerate(movie_info_list):
            with columns[i % 3]:
                st.markdown(
                    f"""
                <div style='display: grid; place-items: center;'>
                    <strong>{movie_info['Name']}</strong>
                    <img src="{movie_info['PosterURL']}" width="250"/>
                </div>
                """,
                    unsafe_allow_html=True,
                )
                st.write("\n")
                st.write("\n")
                st.write("\n")

        st.table(all_data[selected_columns].head(20).rename(columns=column_mapping))

    elif selected_top == "Top 50 Movies":
        top_50_movies = all_data[selected_columns].head(50)

        movie_info_list = []
        for index, movie in top_50_movies.iterrows():
            movie_info = {
                "Name": movie["title"],
                "PosterURL": fetch_poster(movie["movie_id"]),
            }
            movie_info_list.append(movie_info)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("\n")

        columns = st.columns(3)
        for i, movie_info in enumerate(movie_info_list):
            with columns[i % 3]:
                st.markdown(
                    f"""
                <div style='display: grid; place-items: center;'>
                    <strong>{movie_info['Name']}</strong>
                    <img src="{movie_info['PosterURL']}" width="250"/>
                </div>
                """,
                    unsafe_allow_html=True,
                )
                st.write("\n")
                st.write("\n")
                st.write("\n")

        st.table(all_data[selected_columns].head(50).rename(columns=column_mapping))

    elif selected_top == "Top 99 Movies":
        top_99_movies = all_data[selected_columns].head(99)

        movie_info_list = []
        for index, movie in top_99_movies.iterrows():
            movie_info = {
                "Name": movie["title"],
                "PosterURL": fetch_poster(movie["movie_id"]),
            }
            movie_info_list.append(movie_info)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("\n")

        columns = st.columns(3)
        for i, movie_info in enumerate(movie_info_list):
            with columns[i % 3]:
                st.markdown(
                    f"""
                <div style='display: grid; place-items: center;'>
                    <strong>{movie_info['Name']}</strong>
                    <img src="{movie_info['PosterURL']}" width="250"/>
                </div>
                """,
                    unsafe_allow_html=True,
                )
                st.write("\n")
                st.write("\n")
                st.write("\n")

        st.table(all_data[selected_columns].head(99).rename(columns=column_mapping))
