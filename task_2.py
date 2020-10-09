org_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
tgt_list = [el for i, el in enumerate(org_list[1:], 1) if el > org_list[i - 1]]
print(tgt_list)
