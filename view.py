import model
import controller

import streamlit as st
import pandas as pd
import numpy as np

APPINFO = st.container()

if 'API_JSON' not in st.session_state:
    st.session_state['API_JSON'] = None

APPINFO.subheader('Application Info')
#APPINFO.write(st.session_state)

st.title('NSW Transport API')
OVERVIEW = st.container()
OVERVIEW.subheader('Project Overview')
OVERVIEW.write('This is a learning project where I dive into the Transport of NSW API') 
OVERVIEW.write('I am using streamlit to build this web application as a blog') 

STEP1 = st.container()

def UNPICKLE_JSON(Container):
    try:
        st.session_state['API_JSON'] = controller.Unpickle_JSON()
        Container.write(st.session_state['API_JSON'])
    except Exception as e:
        Container.error(e)

STEP1.subheader('Getting Data From The API')
STEP1.write('Here I use the python requests module') 
STEP1.write('You need to register on the Transport NSW Website and get an API Key')
STEP1.write('There is an example of the code in my GIT')
STEP1.write('I have stored the data on a pickle file in the repo, and the app reads from that')
JSON_SAMPLE = STEP1.expander('Click This Button to show the API JSON')
JSON_SAMPLE.button('SHOW ME!', on_click=UNPICKLE_JSON, args=(JSON_SAMPLE, ))


STEP1 = st.container()
STEP1.subheader('Parsing the Data From The API')
STEP1.write('The response module decodes the data into JSON out of the box') 
STEP1.write('We can use a little list comprehension magic to break the json up into different parts.')








