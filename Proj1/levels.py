# levels.py

NorP = "Normal Piece" 
SpeP = "Special Piece" 

beginner_1 = {
    "initial_state": [
        ["NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP"],
        ["SpeP", "NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["SpeP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "SpeP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}


beginner_2 = {
    "initial_state": [
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}

beginner_3 = {
    "initial_state": [
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}


amateur_1 = {
    "initial_state": [
        ["NorP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "NorP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}


amateur_2 = {
    "initial_state": [
        ["NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP"],
        ["NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP"],
        ["SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}

amateur_3 = {
    "initial_state": [
        ["SpeP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "SpeP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["SpeP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "SpeP"],
        ["NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP"],
        ["SpeP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "SpeP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["SpeP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "SpeP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}


expert_1 = {
    "initial_state": [
        ["NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "SpeP", "NorP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}


expert_2 = {
    "initial_state": [
        ["NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "SpeP", "NorP"],
        ["SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP"],
        ["SpeP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "SpeP"],
        ["NorP", "NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP", "NorP"],
        ["SpeP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "SpeP"],
        ["NorP", "NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP", "NorP"],
        ["SpeP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "SpeP"],
        ["SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP"],
        ["NorP", "SpeP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}

expert_3 = {
    "initial_state": [
        ["SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "NorP", "NorP"],
        ["SpeP", "SpeP", "NorP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP", "NorP", "SpeP", "SpeP"],
        ["NorP", "NorP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP", "SpeP"],
        ["NorP", "SpeP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "SpeP", "NorP"],
        ["SpeP", "NorP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "NorP", "SpeP"],
    ],
    "objective_state": [
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "NorP"],
        ["NorP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "NorP"],
        ["NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "SpeP", "SpeP", "SpeP", "SpeP", "SpeP", "NorP", "NorP", "NorP"],
        ["NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP", "NorP"],
    ],
}

# Dicionário de todos os níveis para fácil acesso
levels = {
    "Beginner": [beginner_1, beginner_2, beginner_3],
    "Amateur": [amateur_1, amateur_2, amateur_3],
    "Expert": [expert_1, expert_2, expert_3],
}