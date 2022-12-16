from typing import Tuple

# Description of input data format and scoring system:
# Opponent: A = Rock (1), B = Paper (2), C = Scissors (3)
# Me: X = Rock (1), Y = Paper (2), Z = Scissors (3)
# Outcome: Loss = 0, Draw = 3, Win = 6

# Import the input file
with open('day_2/input_2.txt') as f:
    input_text = f.readlines()

# Create mappings of points for individual choices
points_mappings = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}


def individual_points(player_choices: Tuple[str, str]) -> Tuple[int, int]:
    """
    Returns the number of points for each player in the game based on their choices for a given round in
    part 1 of challenge
    :param player_choices: A tuple containing two strings representing the choice of p1 and p2 for a given round
    :return: A tuple containing integers representing the points scored by p1 and p2 for a given round
    """
    # Assign each players choices to variables
    p1_choice, p2_choice = player_choices
    # Based on the choices of each player calculate the result of the round
    draw = (
            (p1_choice == 'A' and p2_choice == 'X') |
            (p1_choice == 'B' and p2_choice == 'Y') |
            (p1_choice == 'C' and p2_choice == 'Z')
    )
    p1_win = (
            (p1_choice == 'A' and p2_choice == 'Z') |
            (p1_choice == 'B' and p2_choice == 'X') |
            (p1_choice == 'C' and p2_choice == 'Y')
    )
    p2_win = (
            (p1_choice == 'A' and p2_choice == 'Y') |
            (p1_choice == 'B' and p2_choice == 'Z') |
            (p1_choice == 'C' and p2_choice == 'X')
    )
    # Check that the choices result in only a single outcome
    # ie there has to be a result but there cannot be more than 1 result
    assert sum([draw, p1_win, p2_win]) == 1, f'No single outcome for provided choices: {p1_choice=}, {p2_choice=}'
    # Assign points to variables for each player based on the outcome of the given round
    if draw:
        p1_result_points = 3
        p2_result_points = 3
    elif p1_win:
        p1_result_points = 6
        p2_result_points = 0
    elif p2_win:
        p1_result_points = 0
        p2_result_points = 6
    else:
        raise ValueError(f'{p1_choice=}, {p2_choice=}, {draw=}, {p1_win=}, {p2_win=}')
    return points_mappings[p1_choice] + p1_result_points, points_mappings[p2_choice] + p2_result_points


matches = [match.replace('\n', '') for match in input_text]
matches = [tuple(match.split(' ')) for match in matches]
match_points = [individual_points(match) for match in matches]

p1_total_score = sum([match_score[0] for match_score in match_points])
p2_total_score = sum([match_score[1] for match_score in match_points])

printout = f'After {len(input_text)} rounds the final score is:'
printout += f'\n\tOpponent: {p1_total_score} points\n\tMe: {p2_total_score}'
print(printout)


def part_2_points(strategy_guide: Tuple[str, str]) -> Tuple[int, int]:
    p1_choice, required_result = strategy_guide
    if (required_result == 'X') & (p1_choice == 'A'):
        p1_points = 6 + 1
        p2_points = 0 + 3
    elif (required_result == 'X') & (p1_choice == 'B'):
        p1_points = 6 + 2
        p2_points = 0 + 1
    elif (required_result == 'X') & (p1_choice == 'C'):
        p1_points = 6 + 3
        p2_points = 0 + 2
    elif (required_result == 'Y') & (p1_choice == 'A'):
        p1_points = 3 + 1
        p2_points = 3 + 1
    elif (required_result == 'Y') & (p1_choice == 'B'):
        p1_points = 3 + 2
        p2_points = 3 + 2
    elif (required_result == 'Y') & (p1_choice == 'C'):
        p1_points = 3 + 3
        p2_points = 3 + 3
    elif (required_result == 'Z') & (p1_choice == 'A'):
        p1_points = 0 + 1
        p2_points = 6 + 2
    elif (required_result == 'Z') & (p1_choice == 'B'):
        p1_points = 0 + 2
        p2_points = 6 + 3
    elif (required_result == 'Z') & (p1_choice == 'C'):
        p1_points = 0 + 3
        p2_points = 6 + 1
    else:
        raise ValueError(f'{required_result=}')
    return p1_points, p2_points


match_points = [part_2_points(match) for match in matches]

p1_total_score = sum([match_score[0] for match_score in match_points])
p2_total_score = sum([match_score[1] for match_score in match_points])

printout = f'After {len(input_text)} rounds the final score is:'
printout += f'\n\tOpponent: {p1_total_score} points\n\tMe: {p2_total_score}'
print(printout)
