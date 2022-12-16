with open('day_6/input_6.txt') as f:
    string = f.read()


n_distinct_chars = 14


def all_chars_different(input_string: str) -> bool:
    string_len = len(input_string)
    string_set_len = len(set(input_string))
    return string_len == string_set_len


print(f'{len(string)}')

last_n_chars = string[:n_distinct_chars]
char_number = n_distinct_chars
for i, char in enumerate(string[n_distinct_chars:]):
    print(f'{i=}, {char=}, {last_n_chars=}')

    assert len(last_n_chars) == n_distinct_chars
    if all_chars_different(last_n_chars):
        break
    else:
        last_n_chars = last_n_chars[1:] + char

print(f'Start of packet marker at character {i+n_distinct_chars}')
