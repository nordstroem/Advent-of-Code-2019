from aocutil import *

class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Paths:
    def __init__(self):
        self.horizontal_segments = []
        self.vertical_segments = []

    def append_segment(self, current_position, new_position):
        if (new_position[0] == current_position[0]):
            segment = Segment(current_position, new_position) if current_position[1] < new_position[1] else Segment(new_position, current_position)
            self.vertical_segments.append(segment)
        else:
            segment = Segment(current_position, new_position) if current_position[0] < new_position[0] else Segment(new_position, current_position)
            self.horizontal_segments.append(segment)
    

def get_new_position(current_position, movement):
    direction = movement[0]
    length = int(movement[1:])
    if direction == "U":
        return (current_position[0], current_position[1] + length)
    elif direction == "D":
        return (current_position[0], current_position[1] - length)
    elif direction == "R":
        return (current_position[0] + length, current_position[1])
    else:
        return (current_position[0] - length, current_position[1])
    

paths = [line.split(',') for line in read_lines("input3.txt")]
wires = [Paths(), Paths()]

for wire, path in zip(wires, paths):
    current_position = (0, 0)
    for movement in path:
        new_position = get_new_position(current_position, movement)
        wire.append_segment(current_position, new_position)
        current_position = new_position


# Compare horizontal for wire 0 to the vertical in wire 1

segments_pairs = [(wires[0].horizontal_segments, wires[1].vertical_segments), (wires[1].horizontal_segments, wires[0].vertical_segments)]
cross_points = []
for segment_pair in segments_pairs:
    for horizontal_segment in segment_pair[0]:
        for vertical_segment in segment_pair[1]:
            inX = vertical_segment.start[0] >= horizontal_segment.start[0] and vertical_segment.start[0] <= horizontal_segment.end[0]
            inY = horizontal_segment.start[1] >= vertical_segment.start[1] and horizontal_segment.start[1] <= vertical_segment.end[1]
            if (inX and inY ):
                cross_point = (vertical_segment.start[0], horizontal_segment.start[1])
                if (cross_point != (0, 0)):
                    cross_points.append(cross_point)

best_point = min(cross_points, key=lambda a: abs(a[0]) + abs(a[1]))

print(abs(best_point[0]) + abs(best_point[1]))