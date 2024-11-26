import streamlit as st # lets us make a simple web app UI
from scrape import scrape_website

st.title("AI Web Scraper") # makes a title 
url = st.text_input("Enter a website URL: ") # makes a text input

if st.button("Scrape Site"): # checks input
    st.write("Scraping the website") 
    result = scrape_website(url)
    print(result)
