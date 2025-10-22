import time


def up_stair(n: int):
    for i in range(0, n, 1):
        print("#" * i)


def down_stair(n: int):
    for i in range(n, 0, -1):
        print("#" * i)


def final_function(n):
    up_stair(n)
    down_stair(n)


start_time = time.time()
final_function(5)
print(f"Time taken: {time.time() - start_time} s")
