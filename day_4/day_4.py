with open('day_4/input_4.txt') as f:
    elf_pairs = f.readlines()

elf_pairs = [pair.strip('\n').split(',') for pair in elf_pairs]
elf_pairs = [[list(range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) + 1)),
              list(range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1]) + 1))]
             for pair in elf_pairs]

elf_pairs_inclusive = [set(pair[0]).issubset(set(pair[1])) | set(pair[1]).issubset(set(pair[0]))
                       for pair in elf_pairs]

inclusive_schedules = sum(elf_pairs_inclusive)

overlapping_schedules = sum([len(set(pair[0]).intersection(set(pair[1]))) > 0 for pair in elf_pairs])
