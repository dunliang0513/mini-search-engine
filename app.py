import streamlit as st
import time

from search import search_and_return_top_twenty
from advance_search import advance_search_and_return_top_ten, create_embeddings_index

st.title("Mini Search Engine about Tech News")

query = st.text_input("Enter your query here:")
embeddings, urls = create_embeddings_index()

if st.button("Search"):
    # If user has entered a query
    if query:
        start_time = time.time()
        # Perform a basic search and get the top twenty results
        search_results = search_and_return_top_twenty(query)
        # Perform an advanced search and get the top ten results
        advance_search_results = advance_search_and_return_top_ten(query, embeddings, urls)

        end_time = time.time()
        response_time = end_time - start_time
        st.write(f"Response time: {response_time:.2f} seconds")

        # Create two columns
        col1, col2 = st.columns(2)

        # If all the keywords in the query are not found in the database
        col1.header("Basic Search Results")
        if search_results == "No matches found":
            col1.text("No matches found")
        else:
            # Display the basic search results to the user in the first column
            
            for url, score in search_results:
                col1.write(f"URL: {url}")
                col1.text(f"Score: {score}")

        # Display the advanced search results to the user in the second column
        col2.header("Advanced Search Results")
        for url, score in advance_search_results:
            col2.write(f"URL: {url}")
            col2.text(f"Score: {score}")
    else:
        # If the user has not entered a query, display a message
        st.write("Please enter a query and press the search button.")