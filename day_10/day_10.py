import math

with open('day_10/input_10.txt') as f:
    commands = f.readlines()

commands = [(command.split()[0], int(command.split()[1])) if command[:4] == 'addx'
            else (command, ) for command in [line.strip('\n') for line in commands]]

n_cycle = 1
X = 1

cycle_vals = dict()

for command in commands:
    if command[0] == 'noop':
        cycle_vals[n_cycle] = X
        n_cycle += 1
    elif command[0] == 'addx':
        for i in range(2):
            if i == 1:
                cycle_vals[n_cycle] = X
                n_cycle += 1
                X += command[1]
            else:
                cycle_vals[n_cycle] = X
                n_cycle += 1
    else:
        raise ValueError(f'Unexpected command received: {n_cycle=}, {command[0]}')

cycle_nums = [20, 60, 100, 140, 180, 220]
signal_strength_sum = sum([cycle_num * cycle_vals[cycle_num] for cycle_num in cycle_nums])

print(f'Total signal strength across given cycles: {signal_strength_sum}')

row_width = 40
n_rows = int(max(cycle_vals.keys()) / row_width)
rows = [['.' for _ in range(row_width)] for _ in range(n_rows)]

for cycle in cycle_vals.keys():
    row = math.floor(cycle / row_width) if cycle % row_width != 0 else math.floor(cycle / row_width) - 1
    pixel = cycle if cycle < 41 else (cycle % row_width + row_width if cycle % row_width == 0 else cycle % row_width)
    print(f'{cycle=}, {row=}, {pixel=}')
    sprite_pos = list(range(cycle_vals[cycle], cycle_vals[cycle] + 3))
    if pixel in sprite_pos:
        rows[row].pop(pixel)
        rows[row].insert(pixel, '#')

final_string = '\n'.join([''.join(row) for row in rows])

print(f'\n{final_string}')
