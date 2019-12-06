from aocutil import *

total_number = 0

for num in range(273025, 767253 + 1):
    digits = [int(c) for c in str(num)]
    never_decreasing = digits == sorted(digits)
    
    groups = [[digits[0]]]
    for d in digits[1:]:
        if d == groups[-1][0]:
            groups[-1].append(d)
        else:
            groups.append([d])
    
    two_adjacent = any(len(dgs) == 2 for dgs in groups)
    if never_decreasing and two_adjacent:
        total_number = total_number + 1


print(total_number)