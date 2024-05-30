import streamlit as st

from search import search_and_return_top_twenty
from advance_search import advance_search_and_return_top_ten, create_embeddings_index

st.title("Mini Search Engine about Tech News")

query = st.text_input("Enter your query here:")
embeddings, urls = create_embeddings_index()

if st.button("Search"):
    # If user has entered a query
    if query:
        # Perform a basic search and get the top twenty results
        search_results = search_and_return_top_twenty(query)
        # If all the keywords in the query are not found in the database
        if search_results == "No matches found":
            st.text(search_results)
            st.text("Here are the recommendations")
            
            # Return the top ten results from the embeddings index by using txtai
            advance_search_results = advance_search_and_return_top_ten(query, embeddings, urls)
            
            # Display the advanced search results to the user
            for url, score in advance_search_results:
                st.write(f"URL: {url}")
                st.text(f"Score: {score}")
        else:
            # Display the basic search results to the user
            for url, score in search_results:
                st.write(f"URL: {url}")
                st.text(f"Score: {score}")
    else:
        # If the user has not entered a query, display a message
        st.write("Please enter a query and press the search button.")