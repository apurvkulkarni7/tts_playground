import streamlit as st

# Input data for the application
def available_models():
    
    model_list_dict = {
        "none":[],
        "en":["mozilla_tts_en"],
        "de":["mozilla_tts_de"],
        # "mozilla_tts_en"
        }
    
    return model_list_dict

class AppFlags:
    def __init__(self):
        """
        Initialize th4e flag class.
        """
        if "run_counter" not in st.session_state.keys():
            st.session_state["run_counter"] = 0
        if "button_model" not in st.session_state.keys():
            st.session_state["button_model"] = False
        if "button_input" not in st.session_state.keys():
            st.session_state["button_input"] = False
        if "selected_language" not in st.session_state.keys():
            st.session_state["selected_language"] = ""
