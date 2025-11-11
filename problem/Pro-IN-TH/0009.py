input_sequence = input().split()
decode_sequence = input()

A = min(input_sequence)
C = max(input_sequence)
B = sorted(input_sequence)[len(input_sequence) // 2]


for i in decode_sequence:
    if i == "A":
        print(A, end=" ")
    elif i == "B":
        print(B, end=" ")
    elif i == "C":
        print(C, end=" ")
