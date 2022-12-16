# Read in the input file as a string
with open('day_1/input_1.txt') as f:
    string = f.read()

# Split the string up into a list based on a double line separator to get a list of strings
# representing the calories carried by each elf
split_string = string.split('\n\n')


def calorie_count(input_string: str) -> int:
    # Create a list of calories carried by each elf by splitting on line separator
    calorie_list = input_string.split('\n')
    # Convert the strings representing calories to integers
    calorie_list_values = [int(calorie_val) for calorie_val in calorie_list if calorie_val != '']
    # Calculate the total sum of calories being carried
    total_calories = sum(calorie_list_values)
    return total_calories


# Create a dictionary of calories carried by each elf
elves = {i + 1: calorie_count(calorie_string) for i, calorie_string in enumerate(split_string)}

# Find the maximum number of calories carried by an individual elf
max_calories = max(elves.values())

# Search through the dictionary of elves to find the elf that matches the maximum number of calories
for elf, calories in elves.items():
    if calories == max_calories:
        print(f'The elf carrying the most calories is elf {elf} with {calories} calories.')

# Sort the number of calories carried by each elf in descending order and sum the top 3 together
elves_calories_sorted = sorted(list(elves.values()), reverse=True)
top_3_calories = sum(elves_calories_sorted[:3])

print(f'\nThe total number of calories carried by the 3 elves with the most calories is: {top_3_calories}')
