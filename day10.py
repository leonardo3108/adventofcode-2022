instructions = [line.rstrip().split() for line in open('input10.txt')]
#instructions = [line.rstrip().split() for line in open('input10-mini.txt')]

X = 1
cycle = 0
history = [[cycle, X]]
for instruction in instructions:
    cycle += 1
    history.append([cycle, X])
    if instruction[0] == 'addx':
        cycle += 1
        history.append([cycle, X])
        X += int(instruction[1])

signal_strengths = [cycle * X for cycle, X in history[20:221:40]]
print('Part one:', sum(signal_strengths))

print()
print()
print('Part two:')
print()
cycle = 1
for _ in range(6):
    row = ''
    for x in range(40):
        X = history[cycle][1]
        if x in [X-1, X, X+1]:
            row += '#'
        else:
            row += '.'
        cycle += 1
    print(row + '   ', cycle - 1)
print()
