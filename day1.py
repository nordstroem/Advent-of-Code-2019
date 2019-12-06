from aocutil import *

def fuel_requirement(mass):
    req = int(mass  / 3) - 2
    return 0 if req < 0 else req + fuel_requirement(req)

inputs = read_lines("input1.txt", lambda x: fuel_requirement(int(x)))

print(sum(inputs))
