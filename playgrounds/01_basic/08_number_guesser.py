import numpy as np


def gen_random_number():
    min_ran = 1
    max_ran = 8
    numbers = np.random.randint(min_ran, max_ran)
    return numbers, min_ran, max_ran


random_numbers, min_range, max_range = gen_random_number()
hint_number = int(input(f"Enter Any number Between {min_range} to {max_range}: "))
counter = 1

while hint_number != random_numbers:
    try:
        if hint_number == random_numbers:
            break
        else:
            print("Not right\n")
            counter += 1
            hint_number = int(
                input(f"Enter Any number Between {min_range} to {max_range}: ")
            )
    except ValueError:
        print("")

print("Congratulation", f"\nYou Guess {counter} time")
