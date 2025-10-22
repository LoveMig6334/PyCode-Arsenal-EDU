boba_type, boba_gram = input().split()
boba_type = boba_type.capitalize()
boba_gram = int(boba_gram)

tea_tye, sugar_level, tea_volume = input().split()
tea_tye = tea_tye.capitalize()
sugar_level = int(sugar_level)
tea_volume = int(tea_volume)

boba_type_dict = {
    "H": 5,
    "O": 3,
    "J": 2,
}


tea_cal_dict = {
    "R": {1: 12, 2: 18, 3: 25},
    "T": {1: 15, 2: 20, 3: 30},
    "M": {1: 10, 2: 15, 3: 20},
}


tea_cal = tea_cal_dict[tea_tye][sugar_level]
print((tea_cal * tea_volume) + boba_type_dict[boba_type] * boba_gram)
