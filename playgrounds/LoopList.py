import time

numbers_list = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12, 13, 13, 14]


# Time complexity of Big o(n) because we loop through all of member in the list
def remove_same(lst: list) -> list:
    new_list = []
    for member in lst:
        if member not in new_list:
            new_list.append(member)
    return new_list


def find_len(lst: list) -> int:
    length = 0
    for i in lst:
        length += 1
    return length


def find_len_index(lst: list) -> int:
    return lst[-1] - lst[0] + 1


start_time = time.time()
print(remove_same(numbers_list))
print(time.time() - start_time)


range_list = list(range(100000000))

start_time = time.time()
print(f"\nMember: {find_len(range_list)}")
print(f"Time Use of counter function {time.time() - start_time}")

start_time = time.time()
print(f"\nMember: {find_len_index(range_list)}")
print(f"Time Use of index function {time.time() - start_time}")
