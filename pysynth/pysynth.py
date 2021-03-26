import os
import numpy as np

# Local module imports
import utility.file
import sound.note
import sound.synth

def test():
    path = 'examples/final_countdown.json'
    song_data = utility.file.read_json_song(path)

    song = sound.synth.generate_mono_song(song_data)

    export_data = {
        'name': song_data['name'].lower().replace(" ", "_"),
        'samplerate': sound.synth.sample_rate,
        'song': song.astype(np.int16)

    }
    utility.file.write_wave_file(export_data)

# TO-DO: Add docs
def note_frequency():
    print("**********************************************")
    print("***             Note Frequency             ***")
    print("**********************************************")
    note = ''
    
    while True:
        note = input("Please type a note (B4, G#3) or 'q' to quit: ")
        
        if note == 'q':
            print('Alright, see ya!')
            break
        
        frequency = sound.note.generate_note_frequency(note)

        print(f'Boom chicka bow wow, {note.capitalize()} has a frequency of {frequency} hz.')
        print('')

def main():
    os.system('clear')
    test()

if __name__ == "__main__":
    main()