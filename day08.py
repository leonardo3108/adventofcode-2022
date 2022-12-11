rows = []
for line in open('input08.txt'):
    rows.append([int(tree) for tree in line.rstrip()])
height = len(rows)
width = len(rows[0])
columns = []
for row_nr in range(width):
    columns.append([row[row_nr] for row in rows])

def add_visible(i, j, visibles):
    if (i, j) not in visibles:
        visibles.append((i, j))
def find_visibles(orientation, line_nr, line, visibles, house = 10, shift = 0):
    previous = -1
    result = 0
    for position_in_line, tree in enumerate(line):
        if tree > previous:
            if orientation == 'row':
                x = position_in_line + shift
                y = line_nr
            elif orientation == '-row':
                x = len(line) - 1 - position_in_line
                y = line_nr
            elif orientation == 'column':
                x = line_nr
                y = position_in_line + shift
            elif orientation == '-column':
                x = line_nr
                y = len(line) - 1 - position_in_line
            if visibles is not None:
                add_visible(x, y, visibles)
            result += 1
            previous = tree
            if tree >= house:
                return result
    return result

visibles = []
for row_nr, row in enumerate(rows):
    find_visibles('row', row_nr, row, visibles)
    find_visibles('-row', row_nr, row[::-1], visibles)

for column_nr, column in enumerate(columns):
    find_visibles('column', column_nr, column, visibles)
    find_visibles('-column', column_nr, column[::-1], visibles)

print('Part one:', len(visibles))
highest_scenic_score = 0
def calc_scenic_score(rows, columns, x, y):
    row = rows[y]
    column = columns[x]
    house = row[x]
    row_repr = ' '*x + '*' + ' ' * (len(row)-x-1)
    col_repr = ' '*y + '*' + ' ' * (len(column)-y-1)
    visibles = []
    up    = find_visibles('-column', x, columns[x][y - 1::-1], visibles, house, 0)
    for _, j in visibles:
        col_repr = col_repr[:j] + '+' + col_repr[j+1:]
    visibles = []
    left  = find_visibles(   '-row', y,    rows[y][x - 1::-1], visibles, house, 0)
    for i, _ in visibles:
        row_repr = row_repr[:i] + '+' + row_repr[i+1:]
    visibles = []
    right = find_visibles(    'row', y,    rows[y][x + 1:], visibles, house, x + 1)
    for i, _ in visibles:
        row_repr = row_repr[:i] + '+' + row_repr[i+1:]
    visibles = []
    down  = find_visibles( 'column', x, columns[x][y + 1:], visibles, house, y + 1)
    for _, j in visibles:
        col_repr = col_repr[:j] + '+' + col_repr[j+1:]
    scenic_score = up * left * right * down
    print((x, y), '-', house)
    print('\trow   ', str(y) + ':', str(row).replace(', ', ''))
    print('\t' + ' '*len(str(y)) + '     left[' + row_repr + ']right')
    print('\tcolumn', str(x) + ':', str(column).replace(', ', ''))
    print('\t' + ' '*len(str(x)) + '       up[' + col_repr + ']down')
    print('\tup', up, 'x left', left, 'x right', right, 'x down', down, '= score', scenic_score)
    return house,up,left,right,down,scenic_score

for y in range(1, height - 1):
    for x in range(1, width - 1):
        house, up, left, right, down, scenic_score = calc_scenic_score(rows, columns, x, y)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score
            #print((x, y), house, '-> up', up, 'left', left, 'right', right, 'down', down, '-> score', scenic_score)
print('\nHighest scenic score:', highest_scenic_score)

#240 low