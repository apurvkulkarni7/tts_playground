import streamlit as st
import sys
from utils.data import available_models, AppFlags
#, click_button, get_button_state, toggle_button_state
from utils.streamlit_utils import app_model_inference, app_model_selection, checkbox_grid, app_input, click_button, get_button_state

st.cache_data.clear()

# Define default falgs
app_flags = AppFlags()

# Title
st.title("Text-to-Speech Converter")

state = False
state = app_model_selection()

state = False
state,input_text = app_input()   

# if st.button("Generate"):
if state:
    model_list = st.session_state['model_list']
    app_model_inference(model_list,input_text)