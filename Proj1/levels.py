# levels.py

NorP = "Normal Piece" # normal piece
SpeP = "Special Piece" # special piece

level_1 = {
    "initial_state": [
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP],
        [NorP, NorP, NorP, NorP, SpeP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
    ],
    "objective_state": [
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
    ],
}

level_2 = {
    "initial_state": [
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, NorP, SpeP, NorP, NorP, NorP],
        [NorP, SpeP, NorP, NorP, NorP, SpeP, SpeP, NorP, NorP],
        [NorP, NorP, SpeP, NorP, NorP, SpeP, SpeP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, SpeP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
    ],
    "objective_state": [
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
    ],
}

level_3 = {
    "initial_state": [
        [NorP, SpeP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, SpeP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, SpeP],
        [NorP, NorP, NorP, NorP, NorP, NorP, SpeP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, SpeP, NorP],
        [NorP, NorP, NorP, NorP, NorP, SpeP, SpeP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, SpeP, NorP, NorP],
    ],
    "objective_state": [
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, SpeP, SpeP, SpeP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
        [NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP, NorP],
    ],
}
