loop_time = int(input())


name_list = []
weight_list = []

for _ in range(loop_time):
    name, weight = input().split()
    name_list.append(name)
    weight_list.append(int(weight))

n = 0
for i in weight_list:
    if i > 15:
        n += 1

print(n)
max_weight_index = weight_list.index(max(weight_list))
print(name_list[max_weight_index], max(weight_list))
