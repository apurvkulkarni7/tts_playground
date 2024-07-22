from TTS.api import TTS
from IPython.display import Audio, display

global model_list 
model_list = [
            "mozilla_tts_de",
            "mozilla_tts_en"
            ]

class TTSModel:
    def __init__(self, model_name: str):
        """
        Initialize the TTSModel class.
        
        Parameters:
        model (str): Model type.
        """
        self.check_model(model_name)
        self.model_name = model_name
        self.load_model()

    def load_model(self):
        if self.model_name == "mozilla_tts_de":
            self.model = TTS(
                model_name="tts_models/de/thorsten/vits",
                vocoder_path="vocoder_models/de/thorsten/wavegrad",
                progress_bar=False,
                gpu=False
                )
        elif self.model_name == "mozilla_tts_en":
            #tts_models/en/ljspeech/glow-tts
            self.model = TTS(
                model_name="tts_models/en/ljspeech/glow-tts",
                vocoder_path="vocoder_models/universal/libri-tts/wavegrad",
                progress_bar=False,
                gpu=False
                )
    
    def convert(self,text):
        sound_file=f"./{self.model_name}.wav"
        if "mozilla_tts" in self.model_name:
            self.model.tts_to_file(text,file_path=sound_file)
        return sound_file
    
    def check_model(self,model_name):
        if model_name not in model_list:
            raise(f"{model_name} is not supported.")