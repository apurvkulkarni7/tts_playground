import streamlit as st
from models import TTSModel

# Streamlit App
st.title("TTS Playground")

st.sidebar.header("Select TTS Model")
model_name = st.sidebar.selectbox("Model", ["mozilla_tts_de", "mozilla_tts_en"])
tts_model = TTSModel(model_name=model_name)

st.header("Text-to-Speech Converter")
text_input = st.text_area("Enter Text", "Hello, this is a TTS test.")

if st.button("Convert"):
    with st.spinner("Generating speech..."):
        audio = tts_model.convert(text_input)
        st.audio(audio, format='audio/wav')