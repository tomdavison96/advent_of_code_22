from itertools import product
from typing import List

with open('day_8/input_8.txt') as f:
    rows = f.readlines()

rows = [row.replace('\n', '') for row in rows]

n_rows = len(rows)
n_columns = len(rows[0])
columns = [''.join([rows[i][j] for i in range(n_rows)]) for j in range(n_columns)]


def visible_from_before(trees: str, index: int) -> bool:
    if index == 0:
        return True
    else:
        return all([int(tree) < int(trees[index]) for tree in trees[:index]])


def visible_from_after(trees: str, index: int) -> bool:
    if index == len(trees) - 1:
        return True
    else:
        return all([int(tree) < int(trees[index]) for tree in trees[index + 1:]])


def visible(row_index: int, column_index: int, tree_row: str, tree_column: str) -> bool:
    assert tree_row[column_index] == tree_column[row_index]
    visible_from_above = visible_from_before(tree_column, row_index)
    visible_from_below = visible_from_after(tree_column, row_index)
    visible_from_left = visible_from_before(tree_row, column_index)
    visible_from_right = visible_from_after(tree_row, column_index)
    return any([visible_from_above, visible_from_below, visible_from_left, visible_from_right])


visible_count = 0
for i, j in product(range(n_rows), range(n_columns)):
    row = rows[i]
    column = columns[j]
    visible_count += visible(row_index=i, column_index=j, tree_row=row, tree_column=column)

print(f'Of {n_rows * n_columns} total trees, {visible_count} are visible')


def tree_counter(trees: List[str], main_tree: str) -> int:
    count = 0
    for tree in trees:
        count += 1
        if int(tree) >= int(main_tree):
            break
    return count


def visible_before_count(trees: str, index: int) -> int:
    if index == 0:
        return 0
    trees_to_consider = list(reversed(trees[:index]))
    main_tree = trees[index]
    return tree_counter(trees_to_consider, main_tree)


def visible_after_count(trees: str, index: int) -> int:
    if index == len(trees) - 1:
        return 0
    trees_to_consider = list(trees[index + 1:])
    main_tree = trees[index]
    return tree_counter(trees_to_consider, main_tree)


def scenic_score(row_index: int, column_index: int, tree_row: str, tree_column: str) -> int:
    assert tree_row[column_index] == tree_column[row_index]
    visible_above_count = visible_before_count(tree_column, row_index)
    visible_below_count = visible_after_count(tree_column, row_index)
    visible_left_count = visible_before_count(tree_row, column_index)
    visible_right_count = visible_after_count(tree_row, column_index)
    return visible_above_count * visible_below_count * visible_left_count * visible_right_count


scenic_scores = []
for i, j in product(range(n_rows), range(n_columns)):
    row = rows[i]
    column = columns[j]
    scenic_scores += [scenic_score(row_index=i, column_index=j, tree_row=row, tree_column=column)]

print(f'\nOf {n_rows * n_columns} total trees, the highest scenic score is {max(scenic_scores)}')
