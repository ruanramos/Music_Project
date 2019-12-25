VALID_NOTES = ["Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#",
               "Bb", "B", "B#"]

OCTAVE_NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "Bb", "B"]
ALL_NOTES = []
values = [i for i in range(-36, 48)]
for i in range(1, 9):
    octave = list(map(lambda x: x + str(i), OCTAVE_NOTES))
    ALL_NOTES = ALL_NOTES + octave
ALL_NOTES = dict(zip(values, ALL_NOTES))
print(ALL_NOTES)
EQUIVALENT_NOTES = {
    "Cb": "B",
    "C#": "Db",
    "D#": "Eb",
    "E#": "F",
    "F#": "Gb",
    "G#": "Ab",
    "A#": "Bb",
    "B#": "C"
}

OCTAVE_SEMI_TONES = 12  # C to C
OCTAVE_TONES = 6
TONE = 2
SEMI_TONE = 1

semi_tones_from_C = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "Bb": 10,
    "B": 11
}
#self.semiTonesFromC4 = self.semi_tones_from_C4[note]

#tom tom semitom tom tom tom semitom
