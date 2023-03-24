import streamlit as st
import numpy as np


st.header(':heart:')

st.subheader('ciaooo :green[scegli una traccia] ')



if st.button('Album1', key='Album1'):
    options = st.multiselect(
        'Choose a track',
        ['Hotline Bling.mp3', 'One Dance.mp3', 'Too Good (feat Rihanna).mp3'])


if st.button('Album2', key='Album2'):
    options = st.multiselect(
        'Choose a track',
        ['traccia1', 'traccia2', 'traccia3', 'Blue'])


audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()

