import random


def number_generate(i):
    a = random.randint(0, i)
    b = random.randint(0, i)
    return a, b


def multiply_number(a: int, b: int) -> int:
    return a * b


result_list = []
for i in range(2, 10):
    result_list.append(multiply_number(*number_generate(i)))
print(result_list)
