import model

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
st.subheader('Raw data')
st.write(model.x)