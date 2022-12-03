def get_priority(item) -> int:
    if item >= 'a':
        return 1+ord(item)-ord('a')
    else:
        return 27+ord(item)-ord('A')

rucksacks = []
for line in open('input03.txt'):
    line = line.rstrip()
    size = len(line) // 2
    rucksacks.append([line[:size], line[size:]])
priorities = 0
groups = []
for rucksack in rucksacks:
    for item in rucksack[0]:
        if item in rucksack[1]:
            if item not in rucksack:
                rucksack.append(item)
    priority = get_priority(rucksack[2])
    #print(rucksack, priority)
    assert(len(rucksack) == 3)
    priorities += priority
    if groups and len(groups[-1]) < 3:
        groups[-1].append(rucksack)
    else:
        groups.append([rucksack])
print('Part one:', priorities)
priorities = 0
for group in groups:
    for item in group[0][0] + group[0][1]:
        if (item in group[1][0] or item in group[1][1]) and (item in group[2][0] or item in group[2][1]):
            if item not in group:
                group.append(item)
    priority = get_priority(group[3])
    #print(group, priority)
    assert(len(group) == 4)
    priorities += priority
print('Part two:', priorities)
