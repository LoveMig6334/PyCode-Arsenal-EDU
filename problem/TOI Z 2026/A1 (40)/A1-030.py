n: int = int(input())
nums = [int(x) for x in input().split()]

greater_val = []
for i in range(0, n):
    a = nums[i * 2]
    b = nums[2 * i + 1]
    greater_val.append(max(a, b))

total = sum(greater_val)
if len(greater_val) > 1:
    print(f"{' + '.join(map(str, greater_val))} = {total}")
else:
    print(f"{total}")
