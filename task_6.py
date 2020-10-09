from itertools import count, cycle

first_nmb = 3
exit_nmb = 10
for nmb in count(first_nmb):
    if nmb >= exit_nmb:
        break
    print(nmb)

print()

rpt_nmb = 0
rpt_max = 10
my_list = ["as", "DS", "pP"]
for el in cycle(my_list):
    if rpt_nmb >= rpt_max:
        break
    print(el)
    rpt_nmb += 1
