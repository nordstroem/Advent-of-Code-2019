from aocutil import *

class Node:
    def __init__(self, parent):
        self.parent = parent

all_nodes = {"COM": Node(None)}

orbits = [l.split(")") for l in read_lines("input6.txt")]
#orbits = [l.split(")") for l in test_orbits]

for target, planet in orbits:
    if target not in all_nodes:
        all_nodes[target] = Node(None)
    if (planet in all_nodes):
        all_nodes[planet].parent = all_nodes[target]
    else:
        all_nodes[planet] = Node(all_nodes[target])


count_orbits = lambda node: 0 if node.parent == None else 1 + count_orbits(node.parent)

total = 0
for name, node in all_nodes.items():
    total += count_orbits(node)

you_orbit = all_nodes["YOU"].parent
santa_orbit = all_nodes["SAN"].parent

you_paths = []
while you_orbit.parent != None:
    you_paths.append(you_orbit.parent)
    you_orbit = you_orbit.parent
    
santa_paths = []
while santa_orbit.parent != None:
    santa_paths.append(santa_orbit.parent)
    santa_orbit = santa_orbit.parent

intersection = [x for x in you_paths if x in santa_paths][0]

print(you_paths.index(intersection) + santa_paths.index(intersection) + 2)
