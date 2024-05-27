import streamlit as st

from search import search_and_return_top_twenty
from advance_search import advance_search_and_return_top_ten, create_embeddings_index

st.title("Mini Search Engine about Tech News")

query = st.text_input("Enter your query here:")
embeddings, urls = create_embeddings_index()

if st.button("Search"):
    if query:
        search_results = search_and_return_top_twenty(query)
        if search_results == "No matches found":
            st.text(search_results)
            st.text("Here are the recommendations")
            advance_search_results = advance_search_and_return_top_ten(query, embeddings, urls)
            
            for url, score in advance_search_results:
                st.write(f"URL: {url}")
                st.text(f"Score: {score}")
        else:
            for url, score in search_results:
                st.write(f"URL: {url}")
                st.text(f"Score: {score}")
    else:
        st.write("Please enter a query and press the search button.")