# A4 = 440
REFERENCE_FREQUENCY = 440

def generate_note_info(note_info, bpm):
    return {
        'freq': generate_note_frequency(note_info['note']),
        'duration': note_duration(note_info['duration'], bpm)
    }

def note_duration(value, bpm):
    duration_reference = {
        'w': 4,
        'h': 2,
        'q': 1,
        'e': 0.5,
        's': 0.25,
    }

    return (60/bpm) * duration_reference[value]


# This is based on a 12 TET system
# The basic formula for the frequencies of the notes of the equal tempered scale is given by
# fn = f0 * (a)n
#    f0 = the frequency of one fixed note which must be defined.
#    n = the number of half steps away from the fixed note you are.
#    fn = the frequency of the note n half steps away.
#    a = (2)1/12 = the number which when multiplied by itself 12 times equals 2 = 1.059463094359...
def generate_note_frequency(note):
    half_step_difference = count_half_steps(note)
    magic_number = 2**(1.0 / 12)

    return REFERENCE_FREQUENCY * (magic_number**half_step_difference)

# This takes a full note name (C3, Bb8, G#3) and gets the half step difference between the note and A4
def count_half_steps(note):
    note_reference = {
    'C':  -9,
    'C#': -8,
    'Db': -8,
    'D':  -7,
    'D#': -6,
    'Eb': -6,
    'E':  -5,
    'F':  -4,
    'F#': -3,
    'Gb': -3,
    'G':  -2,
    'G#': -1,
    'Ab': -1,
    'A':   0,
    'A#':  1,
    'Bb':  1,
    'B':   2
    }

    note_name = note[0:-1].capitalize()
    note_octave = int(note[-1])
    octave_difference = note_octave - 4

    return note_reference[note_name] + 12 * octave_difference