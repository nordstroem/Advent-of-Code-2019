from aocutil import *
import math
import numpy as np

class Segment:
    def __init__(self, start, end, steps):
        self.start = start
        self.end = end
        self.steps = steps

class Paths:
    def __init__(self):
        self.horizontal_segments = []
        self.vertical_segments = []

    def append_segment(self, current_position, new_position, steps):
        if (new_position[0] == current_position[0]):
            self.vertical_segments.append(Segment(current_position, new_position, steps))
        else:
            self.horizontal_segments.append(Segment(current_position, new_position, steps))
    

def get_new_position(current_position, movement):
    direction = movement[0]
    length = int(movement[1:])
    if direction == "U":
        return current_position + np.array([0, length])
    elif direction == "D":
        return current_position - np.array([0, length])
    elif direction == "R":
        return current_position + np.array([length, 0])
    else:
        return current_position - np.array([length, 0])
    

def within(p, a, b):
    left = a if a < b else b
    right = b if a < b else a
    return p >= left and p <= right

paths = [line.split(',') for line in read_lines("input3.txt")]
#test_lines = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
#paths = [line.split(',') for line in test_lines]

wires = [Paths(), Paths()]

for wire, path in zip(wires, paths):
    current_position = np.array([0,0])
    steps = 0
    for movement in path:
        new_position = get_new_position(current_position, movement)
        wire.append_segment(current_position, new_position, steps)
        steps = steps + int(movement[1:])
        current_position = new_position


segments_pairs = [(wires[0].horizontal_segments, wires[1].vertical_segments), (wires[1].horizontal_segments, wires[0].vertical_segments)]
cross_points = []
minimum_steps = 9999999999999
for segment_pair in segments_pairs:
    for horizontal_segment in segment_pair[0]:
        for vertical_segment in segment_pair[1]:
            inX = within(vertical_segment.start[0], horizontal_segment.start[0], horizontal_segment.end[0])
            inY = within(horizontal_segment.start[1], vertical_segment.start[1], vertical_segment.end[1])
            if (inX and inY):
                cross_point = np.array([vertical_segment.start[0], horizontal_segment.start[1]])
                if (cross_point[0] != 0 and cross_point[1] != 0):
                    v_steps = vertical_segment.steps + int(np.linalg.norm(vertical_segment.start - cross_point))
                    h_steps = horizontal_segment.steps + int(np.linalg.norm(horizontal_segment.start - cross_point))
                    tot_steps = v_steps + h_steps
                    minimum_steps = minimum_steps if tot_steps > minimum_steps else tot_steps
                    cross_points.append(cross_point)

best_point = min(cross_points, key=lambda a: abs(a[0]) + abs(a[1]))

#print(abs(best_point[0]) + abs(best_point[1]))

print(minimum_steps)


