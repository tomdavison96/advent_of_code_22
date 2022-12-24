import math
import numpy as np

with open('day_11/input_11.txt') as f:
    monkeys = f.read().split('\n\n')

monkeys_dict = {monkey: {'items': [int(item.strip()) for item in
                                   [line.strip()
                                    for line in monkeys[monkey].split('\n')][1].strip('Starting items:').split(',')],
                         'inspects': 0
                         }
                for monkey, _ in enumerate(monkeys)
                }

monkeys_dict[0]['worry_calc'] = lambda curr_worry: curr_worry * 2
monkeys_dict[1]['worry_calc'] = lambda curr_worry: curr_worry + 3
monkeys_dict[2]['worry_calc'] = lambda curr_worry: curr_worry + 6
monkeys_dict[3]['worry_calc'] = lambda curr_worry: curr_worry + 5
monkeys_dict[4]['worry_calc'] = lambda curr_worry: curr_worry + 8
monkeys_dict[5]['worry_calc'] = lambda curr_worry: curr_worry * 5
monkeys_dict[6]['worry_calc'] = lambda curr_worry: curr_worry * curr_worry
monkeys_dict[7]['worry_calc'] = lambda curr_worry: curr_worry + 4

monkeys_dict[0]['worry_test'] = lambda curr_worry: 2 if curr_worry % 17 == 0 else 5
monkeys_dict[1]['worry_test'] = lambda curr_worry: 7 if curr_worry % 13 == 0 else 4
monkeys_dict[2]['worry_test'] = lambda curr_worry: 6 if curr_worry % 19 == 0 else 5
monkeys_dict[3]['worry_test'] = lambda curr_worry: 7 if curr_worry % 7 == 0 else 1
monkeys_dict[4]['worry_test'] = lambda curr_worry: 0 if curr_worry % 11 == 0 else 2
monkeys_dict[5]['worry_test'] = lambda curr_worry: 6 if curr_worry % 3 == 0 else 3
monkeys_dict[6]['worry_test'] = lambda curr_worry: 3 if curr_worry % 2 == 0 else 1
monkeys_dict[7]['worry_test'] = lambda curr_worry: 4 if curr_worry % 5 == 0 else 0

num_rounds = 10_000
solving_part = 2
lcm = np.lcm.reduce([17, 13, 19, 7, 11, 3, 2, 5])

for i in range(num_rounds):
    for monkey in monkeys_dict.keys():
        for _ in range(len(monkeys_dict[monkey]['items'])):
            current_item = monkeys_dict[monkey]['items'].pop(0)
            if solving_part == 1:
                current_worry = monkeys_dict[monkey]['worry_calc'](current_item) // 3
            else:
                current_worry = monkeys_dict[monkey]['worry_calc'](current_item) % lcm
            recipient = monkeys_dict[monkey]['worry_test'](current_worry)
            monkeys_dict[monkey]['inspects'] = monkeys_dict[monkey]['inspects'] + 1
            monkeys_dict[recipient]['items'] = monkeys_dict[recipient]['items'] + [current_worry]
    if (i + 1) % (0.01 * num_rounds) == 0:
        print(f'Round {i + 1} of {num_rounds} completed')

monkey_business = math.prod(sorted([monkeys_dict[monkey]['inspects'] for monkey in monkeys_dict.keys()])[-2:])

print(f'After {num_rounds} rounds the level of monkey business is: {monkey_business}')
