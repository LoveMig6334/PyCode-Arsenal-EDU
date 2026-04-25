line_number = int(input())
income_list = []

for i in range(line_number):
    income = int(input())
    income_list.append(income)

print(sum(income_list))
print(max(income_list))
print(min(income_list))
avg = sum(income_list) / line_number
print(f"{avg:.1f}")
