import streamlit as st
import home
import eda
import summary

navigation = st.sidebar.selectbox('Choose Page:',('Home','EDA','Phone Summary'))

if navigation == 'Home':
    home.run()
elif navigation == 'Phone Summary':
    summary.run()
elif navigation == 'EDA':
    eda.run()