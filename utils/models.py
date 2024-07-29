from TTS.api import TTS
from IPython.display import Audio, display
import torch
import streamlit as st
from utils.data import Database

class TTSModel:
    def __init__(self, model: str):
        """
        Initialize the TTSModel class.
        
        Parameters:
        model (str): Model type.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = model
        self.model_data = Database().get_model_data(model)
        self.load_model()
        
    def load_model(self):
        model_full_name = self.model_data['path']
        vocoder_model = self.model_data['vocoder']

        if self.model_data['provider'] == 'coqui':
            self.model = TTS(
                model_name=model_full_name,
                vocoder_path=vocoder_model,
                progress_bar=False
                ).to(self.device)
        
    def convert(self,text):
        sound_file=f"./{self.model_data['name']}.wav"
        
        model_config = {
            "text":text,
            "file_path":sound_file
        }
        
        if self.model.is_multi_lingual:
            model_config["language"] = self.model_data['lang']
        
        if self.model.is_multi_speaker:
            model_config["speaker"] = self.model_data['speaker']

        self.model.tts_to_file(**model_config)
        
        return sound_file