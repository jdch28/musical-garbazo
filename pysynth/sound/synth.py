import numpy as np

# Local module imports
from . import note

sample_rate = 44100
amplitude = np.iinfo(np.int16).max

def get_wave(freq, duration):
    amplitude = np.iinfo(np.int16).max
    t = np.linspace(0.0, float(duration), int(sample_rate*duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def generate_mono_song(song_data):
    bpm = song_data['bpm']

    notes = [note.generate_note_info(note_info, bpm) for note_info in song_data['notes']]

    song = [get_wave(note['freq'], note['duration']) for note in notes]
    song = np.concatenate(song)

    return song
