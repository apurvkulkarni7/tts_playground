from TTS.api import TTS
from IPython.display import Audio, display
import torch
import streamlit as st

class TTSModel:
    def __init__(self, model_data: str):
        """
        Initialize the TTSModel class.
        
        Parameters:
        model (str): Model type.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        #self.check_model(model)
        self.model_data = model_data
        self.load_model()
        

    def load_model(self):
        
        if self.model_data['lang'] == "en":
            # English vocoder model
            # "vocoder_models/en/ljspeech/hifigan_v2"
            # "vocoder_models/universal/libri-tts/wavegrad"
            # "vocoder_models/en/vctk/hifigan_v2"
            # "vocoder_models/en/blizzard2013/hifigan_v2"
            vocoder_model="vocoder_models/en/ljspeech/hifigan_v2"
        if self.model_data['lang'] == "de":
            # German vocoder model
            # "vocoder_models/de/thorsten/wavegrad"
            # "vocoder_models/de/thorsten/fullband-melgan"
            # "vocoder_models/de/thorsten/hifigan_v1"
            vocoder_model="vocoder_models/de/thorsten/hifigan_v1"
        
        
        self.model = TTS(
            model_name=self.model_data['path'],
            vocoder_path=vocoder_model,
            progress_bar=False
            ).to(self.device)

        
        #     self.model = self.model.s("p230")
                
    def convert(self,text):
        sound_file=f"./{self.model_data['name']}.wav"
        
        if self.model.is_multi_lingual:
            self.model.tts_to_file(
                text,
                speaker='Ana Florence',
                language=self.model_data['lang'],
                file_path=sound_file
                )
        elif self.model.is_multi_speaker:
            self.model.tts_to_file(
                text,
                speaker='p234',
                file_path=sound_file
                )
        else:
            self.model.tts_to_file(
                text,
                file_path=sound_file
                )
        return sound_file
    
    # def check_model(self,model_name):
    #     if model_name not in model_list:
    #         raise(f"{model_name} is not supported.")