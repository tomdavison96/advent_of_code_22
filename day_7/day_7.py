from itertools import product

with open('day_7/input_7.txt') as f:
    input_string = f.read()

dirs = {'/': 0}
current_dir = ['/']

for line in input_string.split('\n'):
    line_items = line.split()
    if line == '':
        pass
    elif line_items[0] == '$':
        if line_items[1] == 'current_dir':
            if line_items[2] == '..':
                current_dir.pop()
            elif line_items[2] == '/':
                current_dir = ['/']
            else:
                current_dir.append(line_items[2])
    elif line_items[0] == 'dir':
        dirs[''.join(current_dir) + line_items[1]] = 0
    else:
        dirs[''.join(current_dir)] += int(line_items[0])
        for i in range(1, len(current_dir)):
            dirs[''.join(current_dir[:-i])] += int(line_items[0])

part_1_ans = sum([size for size in dirs.values() if size <= 100000])

print(f'The answer to part 1 is {part_1_ans}')

part_2_ans = min([size for size in dirs.values() if size >= 30000000 - (70000000 - max(dirs.values()))])

print(f'The answer to part 2 is {part_2_ans}')
