from aocutil import *

class Node:
    def __init__(self, parent):
        self.parent = parent

all_nodes = {"COM": Node(None)}

orbits = [l.split(")") for l in read_lines("input6.txt")]

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

print(total) 


# Inject all nodes into a dictionary, taking the string as name
# Build the tree (one parent per node)
# Traverse the tree starting from all nodes in the dictionary, sum the result.