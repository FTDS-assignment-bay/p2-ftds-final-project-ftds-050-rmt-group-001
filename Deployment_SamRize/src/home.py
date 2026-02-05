import streamlit as st
from PIL import Image 

st.set_page_config(
    page_title='Samrize - Samsung Phone Recommender',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    col1, col2, col3 = st.columns([0.1, 0.15, 0.1])
    with col2:
        st.image("src/SamRize_Logo_clear.png", width=5000)

    st.header("Welcome to Samrize!")

    st.write('Having problem to decide what Samsung phone to use?' )

    st.write('Worry no longer, in Samrize we can help you to decide the best phone fot your need by giving you a summary of 20 most recent released Samsung phone.')

    st.write('Come check it out, on our `Phone Summary` option on the sidebar navigation.')

    st.write('And if you are interested in our finding with the data, we also create A Simple Exploratory Data Analysis(EDA), that you can check on our `EDA` option')

if __name__ == '__main__':
    run()