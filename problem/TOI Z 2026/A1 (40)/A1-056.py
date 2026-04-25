point_1 = [int(x) for x in input().split()]
point_2 = [int(x) for x in input().split()]

abs_dis = (
    abs(point_1[0] - point_2[0]) ** 2
    + abs(point_1[1] - point_2[1]) ** 2
    + abs(point_1[2] - point_2[2]) ** 2
) ** 0.5

print(f"{abs_dis:.2f}")
