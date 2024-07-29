from io import StringIO
import streamlit as st
import sys
from utils.models import TTSModel
from utils.data import Database

def click_button(button_name):
    st.session_state[button_name] = True

def get_button_state(button_name):
    return st.session_state[button_name]

def toggle_button_state(button_name):
    if st.session_state[button_name]:
        st.session_state[button_name] = False
    else:
        st.session_state[button_name] = True

# Function to display checkboxes in a grid and return a list of checked items
def checkbox_grid(items, header="Multi grid checkbox", cols=3):
    container = st.container()
    checkbox_states = []
    container.write(header)

    # Divide the checkboxes into the specified number of columns
    for i in range(0, len(items), cols):
        cols_widgets = container.columns(cols)
        for idx, item in enumerate(items[i:i+cols]):
            # Add a checkbox for each item and store its state
            checkbox_state = cols_widgets[idx].checkbox(item)
            checkbox_states.append((item, checkbox_state))

    # Return a list of checked items
    checked_items = [item for item, checked in checkbox_states if checked]
    return checked_items

def app_model_selection():
    state = False
    database = Database()

    languages = []
    languages = database.list_languages()
    languages.insert(0, 'all')  # Add an 'All' option for no filtering
    languages.insert(0, 'none')  # Add an 'none' option

    # Create a dropdown for selecting language
    st.header("Select TTS Model")
    selected_language = st.selectbox('Select Language', languages, label_visibility="visible")
    st.write(selected_language)
    
    if st.session_state["selected_language"] == "":
        st.session_state["button_model"] = False

    # Model selection
    model_selection_text = "Available TTS models"
    if selected_language == "all":
        all_model_list = database.list_all_models() #[ model_i for models in lang_model_list_dict.values() for model_i in models ]
        all_model_list = list(set(all_model_list))
        all_model_list.sort()
        model_list = checkbox_grid(header=model_selection_text, items=all_model_list, cols=4)
    elif selected_language == "none":
        st.write("Please select appropriate option above.")
        model_list=[]
    else:
        model_list = checkbox_grid(header=model_selection_text, items=database.get_models(selected_language), cols=4)

    if len(model_list) == 0:
        st.error('No model selected. Please Select a model.', icon=":material/error:")

    # if st.button("Confirm model selection"):
    st.session_state["button_model"] = True
    st.session_state['selected_language'] = selected_language
    st.session_state['models'] = model_list
    state = True
    
    if st.session_state['selected_language'] != "":
        st.write("Selected models")
        st.text(model_list)
    return state

def app_input():    
    #text_input=""
    manual_input=False
    file_input=False
    
    # if app_flags.button_model:
    with st.form("Input Text"):
        st.header("Input Text")
        input_cols = st.columns(2)
    
        # Text input
        with input_cols[0]:
            text_input = st.text_area("Enter your text", placeholder="Enter your text",label_visibility="hidden")
            if text_input != "":
                manual_input=True
            # File input
            with input_cols[1]:
                uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
                if len(uploaded_files) > 0:
                    file_input = True
                    text_input = ""
                    for uploaded_file in uploaded_files:
                        text_input += StringIO(uploaded_file.getvalue().decode("utf-8")).read()
                        st.write("filename:", uploaded_file.name)

        st.session_state["button_input"] = st.form_submit_button("Convert")     
        if st.session_state["button_input"]:
            if len(text_input) == 0:
                st.error('Minimum length of the  required text is one character', icon=":material/error:")
                sys.exit(1)
            st.text("Provided text:")
            st.text(text_input)
            return True, text_input
        else:
            return False, text_input

def app_model_inference(models : list, text_input: str):
    
    # Define columns and rows in the results
    num_items = len(models)
    num_cols=2
    num_rows=(num_items+1) // num_cols

    with st.spinner("Generating speech..."):
        st.header("Results")
        for row_i in range(num_rows):
            # Layout for displaying results
            cols = st.columns(num_cols,gap="large")
            for col_i in range(num_cols):
                with cols[col_i]:
                    try:
                        model_i = models[num_cols*row_i+col_i]
                    except:
                        continue
                    st.write(model_i)
                    
                    #if "mozilla_tts" in model_i:
                    tts_model = TTSModel(model_i)
                    audio = tts_model.convert(text_input)
                    
                    st.audio(audio, format='audio/wav')