from typing import List, Dict

from Note import Note

VALID_NOTES = ["Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B", "B#"]

# Using MIDI notation
NOTES = {}


# Using scientific pitch notation. More info at https://en.wikipedia.org/wiki/Scientific_pitch_notation
Cb1 = Note("C", 1, "b")
C1 = Note("C", 1)
CS1 = Note("C", 1, "#")
Cb2 = Note("C", 2, "b")
C2 = Note("C", 2)
CS2 = Note("C", 2, "#")
Cb3 = Note("C", 3, "b")
C3 = Note("C", 3)
CS3 = Note("C", 3, "#")
Cb4 = Note("C", 4, "b")
C4 = Note("C", 4)
CS4 = Note("C", 4, "#")
Cb5 = Note("C", 5, "b")
C5 = Note("C", 5)
Cb6 = Note("Cb", 6)
C6 = Note("C", 6)
Cb7 = Note("Cb", 7)
C7 = Note("C", 7)
Cb8 = Note("Cb", 8)
C8 = Note("C", 8)
Db1 = Note("Db", 1)
D1 = Note("D", 1)
D2 = Note("D", 2)
D3 = Note("D", 3)
D4 = Note("D", 4)
D5 = Note("D", 5)
D6 = Note("D", 6)
D7 = Note("D", 7)
E1 = Note("E", 1)
E2 = Note("E", 2)
E3 = Note("E", 3)
E4 = Note("E", 4)
E5 = Note("E", 5)
E6 = Note("E", 6)
E7 = Note("E", 7)
F1 = Note("F", 1)
F2 = Note("F", 2)
F3 = Note("F", 3)
F4 = Note("F", 4)
F5 = Note("F", 5)
F6 = Note("F", 6)
F7 = Note("F", 7)
G1 = Note("G", 1)
G2 = Note("G", 2)
G3 = Note("G", 3)
G4 = Note("G", 4)
G5 = Note("G", 5)
G6 = Note("G", 6)
G7 = Note("G", 7)
A1 = Note("A", 1)
A2 = Note("A", 2)
A3 = Note("A", 3)
A4 = Note("A", 4)
A5 = Note("A", 5)
A6 = Note("A", 6)
A7 = Note("A", 7)
B1 = Note("B", 1)
B2 = Note("B", 2)
B3 = Note("B", 3)
B4 = Note("B", 4)
B5 = Note("B", 5)
B6 = Note("B", 6)
B7 = Note("B", 7)

C = Note("C")
D = Note("D")
E = Note("E")
F = Note("F")
G = Note("G")
A = Note("A")
B = Note("B")

FIRST_OCTAVE: List[Note] = [C1, D1, E1, F1, G1, A1, B1, C2]
SECOND_OCTAVE: List[Note] = [C2, D2, E2, F2, G2, A2, B2, C3]
THIRD_OCTAVE: List[Note] = [C3, D3, E3, F3, G3, A3, B3, C4]
FOURTH_OCTAVE: List[Note] = [C4, D4, E4, F4, G4, A4, B4, C5]
FITH_OCTAVE: List[Note] = [C5, D5, E5, F5, G5, A5, B5, C6]
SIXTH_OCTAVE: List[Note] = [C6, D6, E6, F6, G6, A6, B6, C7]
SEVENTH_OCTAVE: List[Note] = [C7, D7, E7, F7, G7, A7, B7, C8]

OCTAVES: Dict[int, List[Note]] = {1: FIRST_OCTAVE, 2: SECOND_OCTAVE, 3: THIRD_OCTAVE, 4: FOURTH_OCTAVE, 5: FITH_OCTAVE, 6: SIXTH_OCTAVE, 7: SEVENTH_OCTAVE}

C_MAJOR_SCALE = [C, D, E, F, G, A, B, C]
D_MAJOR_SCALE = [D, E, F, G, A, B, C]