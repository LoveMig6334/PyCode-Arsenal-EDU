card_input = input()

if len(card_input) == 3:
    number, char = card_input[0:2], card_input[2:3]
elif len(card_input) == 2:
    number, char = card_input[0:1], card_input[1:2]

number_char: dict = {
    "A": "ace",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10",
    "J": "jack",
    "Q": "queen",
    "K": "king",
}


char_dict_match: dict = {
    "D": "diamonds",
    "H": "hearts",
    "S": "spades",
    "C": "clubs",
}

print(f"{number_char[number]} of {char_dict_match[char.capitalize()]}")
