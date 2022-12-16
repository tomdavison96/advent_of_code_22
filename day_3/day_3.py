from typing import List

# Read input file in by each line
with open('day_3/input.txt') as f:
    rucksacks = f.readlines()

# Clean each rucksack by removing line separator from the string
rucksacks = [rucksack.strip('\n') for rucksack in rucksacks]

rucksacks_compartments = [{'compartment_1': rucksack[:len(rucksack) // 2],
                           'compartment_2': rucksack[len(rucksack) // 2:]}
                          for rucksack in rucksacks]

assert all([len(rucksack['compartment_1']) == len(rucksack['compartment_2']) for rucksack in rucksacks_compartments])

common_items = [set(rucksack['compartment_1']).intersection(set(rucksack['compartment_2']))
                for rucksack in rucksacks_compartments]

assert all([len(common_item) == 1 for common_item in common_items])

common_items = [list(common_item)[0] for common_item in common_items]

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
character_scores = {character: i + 1 for i, character in enumerate(characters)}

total_score = sum([character_scores[common_item] for common_item in common_items])

rucksack_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]


def common_characters(list_of_strings: List[str]) -> List:
    common_chars = list(set(list_of_strings[0]).intersection(list_of_strings[1]))
    if len(list_of_strings) <= 2:
        return common_chars
    else:
        for string in list_of_strings[2:]:
            common_chars = set(common_chars).intersection(set(string))
        return common_chars


rucksack_characters = [list(common_characters(rucksack_group)) for rucksack_group in rucksack_groups]

assert all([len(rucksack_character) == 1 for rucksack_character in rucksack_characters])

rucksack_character_score = [character_scores[rucksack_character[0]] for rucksack_character in rucksack_characters]

total_score_groups = sum(rucksack_character_score)
