org_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for i, el in enumerate(org_list) if org_list.count(el) == 1])
