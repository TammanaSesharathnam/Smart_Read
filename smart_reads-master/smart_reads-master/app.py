import pickle
import os
import streamlit as st
import numpy as np

st.header("Book Recommendation System using Collaborative Filtering")
os.makedirs('artifacts', exist_ok=True)

# Load the saved models and data
try:
    with open('artifacts/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('artifacts/books_name.pkl', 'rb') as f:
        book_name = pickle.load(f)
    with open('artifacts/final_rating.pkl', 'rb') as f:
        final_rating = pickle.load(f)
    with open('artifacts/books_pivot.pkl', 'rb') as f:
        book_pivot = pickle.load(f)
except FileNotFoundError:
    st.error("Required model files not found. Please ensure all model artifacts are present.")
    st.stop()

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
    
    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)
    
    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)
    
    return poster_url

def recommend_book(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)    

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    
    return book_list, poster_url

# Main UI
st.title("Book Recommender System")

selected_book = st.selectbox(
    "Type or select a book",
    book_name
)

if st.button('Show Recommendation'):
    try:
        recommendation_books, poster_url = recommend_book(selected_book)
        
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommendation_books[i+1])
                st.image(poster_url[i+1])
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    