chromo_len = int(input())
chromo_1 = input().split()
chromo_2 = input().split()

edit_times = int(input())

edit_code_lst = []
for _ in range(edit_times):
    edit_code = input().split()
    edit_code_lst.append(edit_code)

for edit_code in edit_code_lst:
    cho_num, gene, replace = edit_code

    if cho_num == "1":
        chromo_1[int(gene)] = replace
    elif cho_num == "2":
        chromo_2[int(gene)] = replace


print(" ".join(chromo_1))
print(" ".join(chromo_2))

wrong_pair = 0

for gene1, gene2 in zip(chromo_1, chromo_2):
    A = (gene1 == "A" or gene2 == "A") and (gene1 == "T" or gene2 == "T")
    B = (gene1 == "C" or gene2 == "C") and (gene1 == "G" or gene2 == "G")

    if not (A or B):
        wrong_pair += 1

print(wrong_pair)
