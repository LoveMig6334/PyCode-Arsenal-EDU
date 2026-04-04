def condition_main(paid: int):
    if paid > 50000:
        str_massage = r"You are eligible for the 10% discount on your purchase."
        discount_amount = float(paid * 0.9)
        return str_massage, discount_amount
    elif paid > 30000:
        str_massage = r"You are eligible for the 5% discount on your purchase."
        discount_amount = float(paid * 0.95)
        return str_massage, discount_amount
    else:
        return "You are not eligible for any discount on your purchase."


paid = int(input("Enter The Price You have Pay: "))
final_str, final_paid = condition_main(paid)
print(f"{final_str} Final Payment: {final_paid}")
