from math import ceil
from collections import deque

mode = 'queue'
grid = []
qugrid = []
for line in open('input05.txt'):
    line = line.rstrip()
    if mode == 'queue':
        if line:
            cell_size = 4
            qtty_cells = ceil(len(line) / cell_size)            
            cells = [line[cell_nr * cell_size:(cell_nr+1) * cell_size].strip().replace('[', '').replace(']', '') for cell_nr in range(0, qtty_cells)]
            if '1' in line:
                stack_names = cells
            else:
                grid.append(cells)
        else:
            mode = 'routine'
            instructions = []
    else:
        fields = line.split()
        instructions.append([fields[3], fields[5], int(fields[1])])
stacks = {}
stacks_two = {}

for stack_number, stack_name in enumerate(stack_names):
    stacks[stack_name] = deque()
    stacks_two[stack_name] = deque()
    for line in grid[::-1]:
        cell = line[stack_number]
        if cell:
            stacks[stack_name].append(cell)
            stacks_two[stack_name].append(cell)

def make_moves(instructions, stacks, multiple, stack_names):
    for stack_from, stack_to, move_quantity in instructions:
        #print(stacks[stack_from], '=', move_quantity, '=>', stacks[stack_to])
        moved_multiple = deque()
        for _ in range(move_quantity):
            moved_one = stacks[stack_from].pop()
            if multiple:
                moved_multiple.append(moved_one)
            else:
                stacks[stack_to].append(moved_one)
        if multiple:
            for _ in range(move_quantity):
                moved_one = moved_multiple.pop()
                stacks[stack_to].append(moved_one)
        #print('\t', stacks[stack_from], '==>', stacks[stack_to])
    return ''.join([stacks[stack_name].pop() for stack_name in stack_names])

#print(stacks)
top_crates = make_moves(instructions, stacks, False, stack_names)
print('Part one:', top_crates)

#print(stacks_two)
top_crates = make_moves(instructions, stacks_two, True, stack_names)
print('Part two:', top_crates)


