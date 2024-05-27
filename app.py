import streamlit as st

from search import search_and_return_top_twenty


st.title("Mini Search Engine about Tech News")

query = st.text_input("Enter your query here:")

if st.button("Search"):
    if query:
        results = search_and_return_top_twenty(query)
        if results == "No matches found":
            st.write(results)
        else:
            for url, score in results:
                st.write(f"URL: {url}, Score: {score}")
    else:
        st.write("Please enter a query and press the search button.")