import os

# Local module imports
import sound.note


def main():
    os.system('clear')
    note_frequency()

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

if __name__ == "__main__":
    main()