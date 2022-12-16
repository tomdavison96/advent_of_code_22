import re
from typing import List, Dict

complete_part = 2

with open('day_5/input.txt') as f:
    initial_text = f.readlines()

crates_text = initial_text[:8]
crates_text = [line.strip('\n') for line in crates_text]

box_width = 3
columns = 9
parsed_lines = {index: [crates_text[index][i:i+box_width+1][:-1]
                        for i in range(0, len(crates_text[index]), box_width+1)]
                for index, _ in enumerate(crates_text)}
parsed_columns = {column: [line[column] for line in parsed_lines.values()]
                  for column in range(columns)}
parsed_columns = {column + 1: list(reversed(parsed_columns[column])) for column in parsed_columns.keys()}
parsed_columns = {column: [value for value in parsed_columns[column] if ' ' not in value] for column in parsed_columns.keys()}

instructions_text = initial_text[10:]
instructions = [re.findall(r'\d+', instruction) for instruction in instructions_text]


def complete_instruction(column_dict: Dict, instruction: List[int], part: int) -> Dict:
    # Find required instructions
    number_to_move = int(instruction[0])
    col_to_move_from = int(instruction[1])
    col_to_move_to = int(instruction[2])

    # Produce explanatory printout
    print(f'\tMoving {number_to_move} crates from column {col_to_move_from} to column {col_to_move_to}')

    # Check that there are enough crates to move
    assert number_to_move <= len(column_dict[col_to_move_from]), f'\n{column_dict}'

    if part == 1:
        # Complete instructions one by one
        number_moved = 0
        while number_moved < number_to_move:
            crate_to_move = column_dict[col_to_move_from].pop()
            print(f'\t\tMoving Crate: {crate_to_move}')
            column_dict[col_to_move_to] = column_dict[col_to_move_to] + [crate_to_move]
            number_moved += 1
    elif part == 2:
        crates_to_move = column_dict[col_to_move_from][-number_to_move:]
        print(f'\t\tMoving Crates: {crates_to_move}')
        column_dict[col_to_move_from] = column_dict[col_to_move_from][:-number_to_move]
        column_dict[col_to_move_to] = column_dict[col_to_move_to] + crates_to_move
    else:
        raise ValueError('part must equal 1 or 2')
    return column_dict


final_columns = {k: v for k, v in parsed_columns.items()}
for i, instruction in enumerate(instructions):
    print(f'\nInstruction {i+1} of {len(instructions)}:')
    final_columns = complete_instruction(final_columns, instruction, part=complete_part)

final_top_crates = [final_columns[column][-1] for column in final_columns.keys()]

print(f'\nFinal Crates at Top: {final_top_crates}')
