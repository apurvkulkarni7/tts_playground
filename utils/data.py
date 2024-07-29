import streamlit as st
import json

# Input data for the application
class Database():
    def __init__(self):
        self.load_database()
    
    def load_database(self):
        f = open('./utils/data.json')
        self.database = json.load(f)
        f.close()

    def list_languages(self):
        lang_list_tmp = [ model_i['lang'] for model_i in self.database.values() ]
        lang_list = list(set([item for sublist in lang_list_tmp for item in (sublist if isinstance(sublist, list) else [sublist])]))
        lang_list.sort()
        return lang_list
    
    def get_models(self, language):
        return [ key for key,value in self.database.items() if value['lang'] == language or language in value['lang'] ]
    
    def list_all_models(self):
        return list(self.database.keys())
    
    def get_model_data(self, model: str):
        return self.database[model]

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

# XTTSV2 speakerlist
########################
#['Claribel Dervla', 'Daisy Studious', 'Gracie Wise', 'Tammie Ema', 'Alison Dietlinde', 'Ana Florence', 'Annmarie Nele', 'Asya Anara', 'Brenda Stern', 'Gitta Nikolina', 'Henriette Usha', 'Sofia Hellen', 'Tammy Grit', 'Tanja Adelina', 'Vjollca Johnnie', 'Andrew Chipper', 'Badr Odhiambo', 'Dionisio Schuyler', 'Royston Min', 'Viktor Eka', 'Abrahan Mack', 'Adde Michal', 'Baldur Sanjin', 'Craig Gutsy', 'Damien Black', 'Gilberto Mathias', 'Ilkin Urbano', 'Kazuhiko Atallah', 'Ludvig Milivoj', 'Suad Qasim', 'Torcull Diarmuid', 'Viktor Menelaos', 'Zacharie Aimilios', 'Nova Hogarth', 'Maja Ruoho', 'Uta Obando', 'Lidiya Szekeres', 'Chandra MacFarland', 'Szofi Granger', 'Camilla Holmström', 'Lilya Stainthorpe', 'Zofija Kendrick', 'Narelle Moon', 'Barbora MacLean', 'Alexandra Hisakawa', 'Alma María', 'Rosemary Okafor', 'Ige Behringer', 'Filip Traverse', 'Damjan Chapman', 'Wulf Carlevaro', 'Aaron Dreschner', 'Kumar Dahl', 'Eugenio Mataracı', 'Ferran Simen', 'Xavier Hayasaka', 'Luis Moray', 'Marcos Rudaski']

# VITS
#######################
# 'ED\n': 0, 'p225': 1, 'p226': 2, 'p227': 3, 'p228': 4, 'p229': 5, 'p230': 6, 'p231': 7, 'p232': 8, 'p233': 9, 'p234'*: 10, 'p236': 11, 'p237': 12, 'p238': 13, 'p239': 14, 'p240': 15, 'p241': 16, 'p243': 17, 'p244': 18, 'p245': 19, 'p246': 20, 'p247': 21, 'p248': 22, 'p249': 23, 'p250': 24, 'p251': 25, 'p252': 26, 'p253': 27, 'p254': 28, 'p255': 29, 'p256': 30, 'p257': 31, 'p258': 32, 'p259': 33, 'p260': 34, 'p261': 35, 'p262': 36, 'p263': 37, 'p264': 38, 'p265': 39, 'p266': 40, 'p267': 41, 'p268': 42, 'p269': 43, 'p270': 44, 'p271': 45, 'p272': 46, 'p273'*: 47, 'p274': 48, 'p275': 49, 'p276': 50, 'p277': 51, 'p278': 52, 'p279': 53, 'p280': 54, 'p281': 55, 'p282': 56, 'p283': 57, 'p284': 58, 'p285': 59, 'p286': 60, 'p287': 61, 'p288': 62, 'p292': 63, 'p293': 64, 'p294': 65, 'p295': 66, 'p297': 67, 'p298': 68, 'p299': 69, 'p300': 70, 'p301': 71, 'p302': 72, 'p303': 73, 'p304': 74, 'p305': 75, 'p306': 76, 'p307': 77, 'p308': 78, 'p310': 79, 'p311': 80, 'p312': 81, 'p313': 82, 'p314': 83, 'p316': 84, 'p317': 85, 'p318': 86, 'p323': 87, 'p326': 88, 'p329': 89, 'p330': 90, 'p333': 91, 'p334': 92, 'p335': 93, 'p336': 94, 'p339': 95, 'p340': 96, 'p341': 97, 'p343': 98, 'p345': 99, 'p347': 100, 'p351': 101, 'p360': 102, 'p361': 103, 'p362': 104, 'p363': 105, 'p364': 106, 'p374': 107, 'p376': 108

# English vocoder model
# "vocoder_models/en/ljspeech/hifigan_v2"
# "vocoder_models/universal/libri-tts/wavegrad"
# "vocoder_models/en/vctk/hifigan_v2"
# "vocoder_models/en/blizzard2013/hifigan_v2"

# German vocoder model
# "vocoder_models/de/thorsten/wavegrad"
# "vocoder_models/de/thorsten/fullband-melgan"
# "vocoder_models/de/thorsten/hifigan_v1"