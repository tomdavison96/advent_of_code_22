from typing import Tuple
import math

with open('day_9/input_9.txt') as f:
    instructions = [tuple(line.split()) for line in f.readlines()]

instructions = [tuple([instruction[0], int(instruction[1])]) for instruction in instructions]


def move_head(current_x: int, current_y: int, move_direction: str) -> Tuple[int, int]:
    """Move the head of the rope in the given move_direction by 1 unit and return the new x, y coordinates"""
    if move_direction == 'L':
        current_x -= 1
    elif move_direction == 'R':
        current_x += 1
    elif move_direction == 'U':
        current_y += 1
    elif move_direction == 'D':
        current_y -= 1
    else:
        raise ValueError(f'Unexpected move_direction provided: {move_direction}')
    return current_x, current_y


def move_tail(tail_x: int, tail_y: int, head_x: int, head_y: int) -> Tuple[int, int]:
    """Move the tail of the rope based on the current position of the head of the rope"""
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    assert max([abs(x_diff), abs(y_diff)]) <= 2, f'Pre tail move {x_diff=}, {y_diff=}'
    if x_diff == 0 and abs(y_diff) == 2:
        tail_y += math.copysign(1, y_diff)
    elif abs(x_diff) == 2 and y_diff == 0:
        tail_x += math.copysign(1, x_diff)
    elif (abs(x_diff) == 1 and abs(y_diff) == 2) or (abs(y_diff) == 1 and abs(x_diff) == 2) or (abs(y_diff) == 2 and abs(x_diff) == 2):
        tail_x += math.copysign(1, x_diff)
        tail_y += math.copysign(1, y_diff)
    elif (x_diff == 0 and y_diff == 0) or (abs(x_diff) == 1 and y_diff == 0) or (x_diff == 0 and abs(y_diff) == 1) or (abs(x_diff) == 1 and abs(y_diff) == 1):
        pass
    else:
        raise ValueError(f'Unexpected result. Tail Coords: ({tail_x}, {tail_y}), Head Coords: ({head_x, head_y}). '
                         f'{x_diff=}, {y_diff=}')
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    assert max([abs(x_diff), abs(y_diff)]) <= 1, f'Post tail move {x_diff=}, {y_diff=}'
    return tail_x, tail_y


x, y = 0, 0
head_locations = [(x, y)]
current_tail_x, current_tail_y = 0, 0
tail_locations = [(current_tail_x, current_tail_y)]
for instruction in instructions:
    direction, distance = instruction
    for i in range(distance):
        x, y = move_head(x, y, direction)
        head_locations += [(x, y)]
        current_tail_x, current_tail_y = move_tail(current_tail_x, current_tail_y, x, y)
        tail_locations += [(current_tail_x, current_tail_y)]

print(f'After following all instructions the head was moved {len(head_locations)} times '
      f'and the tail visited {len(set(tail_locations))} unique locations')


x, y = 0, 0
head_locations = [(x, y)]
tail_locations = [(x, y)]
rope_length = 10
rope_positions = [(x, y)] * rope_length
for instruction in instructions:
    direction, distance = instruction
    for _ in range(distance):
        x, y = rope_positions.pop(0)
        x, y = move_head(x, y, direction)
        head_locations = [(x, y)]
        rope_positions.insert(0, (x, y))
        assert len(rope_positions) == 10
        for knot in range(1, rope_length):  # Iterate through other parts of the rope and treat each one as a 'tail'
            current_head_x, current_head_y = rope_positions[knot - 1]
            current_tail_x, current_tail_y = rope_positions.pop(knot)
            current_tail_x, current_tail_y = move_tail(current_tail_x, current_tail_y, current_head_x, current_head_y)
            rope_positions.insert(knot, (current_tail_x, current_tail_y))
            assert len(rope_positions) == 10
        tail_locations += [rope_positions[-1]]

print(f'After following all instructions the head was moved {len(head_locations)} times '
      f'and the tail visited {len(set(tail_locations))} unique locations')
