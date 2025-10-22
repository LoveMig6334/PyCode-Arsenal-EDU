def findmean(a):
    res = [sum(idx) for idx in zip(*a)]
    final_set = []
    for i in range(3):
        final_set.append(res[i] / 3)
    return final_set


print(findmean([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
