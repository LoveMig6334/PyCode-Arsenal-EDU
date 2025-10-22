# โจทย์
# ให้สร้างฟังก์ชั่นในการตัดเกรดและฟังก์ชั่นในการคำนวนหาค่าbmi จากนั้นให้สร้างโปรแกรมในการเลือกเรียกใช้ฟังก์ชั่นเหล่านั้นอีกที
mass = int(input("Enter body mass: "))
hight = int(input("Enter hight: "))


def bmi(mass, hight):
    bmi = mass / (hight / 100) ** 2
    return int(bmi)


score = int(input("Enter test score: "))


def grade(score):
    if score >= 80:
        return "You got A"
    elif score >= 70:
        return "you got B"
    elif score >= 60:
        return "you got C"
    elif score >= 50:
        return "you got D"
    else:
        return "You fail test"


print(f"You got Grade {grade(score)} in test ")
print(f"This is your BMI score {bmi(mass, hight)}")
