nums = []
for i in range(3):
    nums.append(int(input()))
    print(f"Input number {i + 1} stored.")

choice = int(input())
if choice == 1:
    print(f"Original order: {' '.join(map(str, nums))}")
elif choice == 2:
    print(f"Descending order: {' '.join(map(str, sorted(nums, reverse=True)))}")
elif choice == 3:
    print(f"Ascending order: {' '.join(map(str, sorted(nums)))}")
