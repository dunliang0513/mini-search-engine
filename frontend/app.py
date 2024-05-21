import streamlit as st


st.title("Mini Search Engine about Tech News")

query = st.text_input("Enter your query here:")

if st.button("Search"):
    if query:
        st.write("Search results for: ", query)
    else:
        st.write("Please enter a query and press the search button.")