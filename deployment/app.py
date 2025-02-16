# import library
import streamlit as st
import eda
import prediction

with st.sidebar:
    st.title('Navigation')
    navigation = st.selectbox('Page', ['Explore', 'Predict Celestial Object Dispositions'])

    st.write('___')
    st.title('About')
    st.write('This web app is used to predict whether a Kepler Object of Interest is an exoplanet or not.')

if navigation == 'Explore':
    eda.run()
else:
    prediction.run()