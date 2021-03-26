import json
from scipy.io import wavfile

def read_json_song(path):
    with open(path) as json_file:
        data = json.load(json_file)
    
    return data

def write_wave_file(data):
    wavfile.write(f"export/{data['name']}.wav", data['samplerate'], data['song'])