import streamlit as st
from models import TTSModel
import sys

model_list = [
    "mozilla_tts_de",
    "mozilla_tts_en",
    # "mozilla_tts_en"
    ]

num_items=len(model_list)
num_cols=2
num_rows=(num_items+1) // num_cols

# Title
st.title("Text-to-Speech Converter")
st.header("Input Text")
text_input = st.text_area("Enter your text", placeholder="Enter your text",label_visibility="hidden")
my_button = st.button("Convert")

if my_button:
    st.text("Provided text:")
    st.text(text_input)
    
    if len(text_input) == 0:
        st.error('Minimum length of the  required text is one character', icon=":material/error:")
        sys.exit(1)
if my_button:    
        
    with st.spinner("Generating speech..."):
        st.header("Results")

        for row_i in range(num_rows):

            # Layout for displaying results
            cols = st.columns(num_cols,gap="large")

            for col_i in range(num_cols):
                with cols[col_i]:
                    
                    try:
                        model_i = model_list[num_cols*row_i+col_i]
                    except:
                        continue
                    
                    st.write(model_i)
                    
                    tts_model = TTSModel(model_name=model_i)
                    audio = tts_model.convert(text_input)
                    st.audio(audio, format='audio/wav')            
        
