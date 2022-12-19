# parse the file
paths = []
for line in open('input14.txt'):
    path =[]
    for point in line.rstrip().split(' -> '):
        x, y = point.split(',')
        path.append((int(x), int(y)))
    paths.append(path)
#print(paths)

# find the rocks
cave_map = {}
cave_range = [999, 0, 999, 0]
for path in paths:
    previous_x, previous_y = 0, 0
    for x, y in path:
        if (x, y) not in cave_map:
            cave_map[(x, y)] = '#'
            if y > cave_range[1]:
                cave_range[1] = y
            elif y < cave_range[0]:
                cave_range[0] = y
            if x > cave_range[3]:
                cave_range[3] = x
            elif x < cave_range[2]:
                cave_range[2] = x
        if previous_x and previous_y:
            assert x == previous_x or y == previous_y
            if x == previous_x:
                for py in range(min(y, previous_y) + 1, max(y, previous_y)):
                    cave_map[(x, py)] = '#'
            elif y == previous_y:
                for px in range(min(x, previous_x) + 1, max(x, previous_x)):
                    cave_map[(px, y)] = '#'
        previous_x, previous_y = x, y

def show_cave(cave_map, cave_range):
    air_line = '.' * (cave_range[3] - cave_range[2] + 1)
    for y in range(cave_range[0], cave_range[1] + 1):
        cave_line = air_line
        for cx, cy in cave_map:
            if cy == y:
                x = cx - cave_range[2]
                cave_line = cave_line[:x] + cave_map[(cx, y)] + cave_line[x + 1:]
        print(cave_line, y)

def send_sand(sand_source, cave_map, cave_range, part):
    x, y = sand_source
    if x < cave_range[2]:
        cave_range[2] = x
    if x > cave_range[3]:
        cave_range[3] = x
    if y < cave_range[0] - 1:
        return send_sand((x, cave_range[0] - 1), cave_map, cave_range, part)
    if y > cave_range[1] and part == 1:
            return None  #fall
    if y >= cave_range[1] and part == 2:
        cave_map[(x, y)] = 'o'
        return (x, y)
    if (x, y + 1) not in cave_map:
        return send_sand((x, y + 1), cave_map, cave_range, part)
    if (x - 1, y + 1) not in cave_map:
        return send_sand((x - 1, y + 1), cave_map, cave_range, part)
    if (x + 1, y + 1) not in cave_map:
        return send_sand((x + 1, y + 1), cave_map, cave_range, part)
    cave_map[(x, y)] = 'o'
    if y < cave_range[0]:
        cave_range[0] = y
    return (x, y)

result = sand_source = (500, 0)
units = -1
while result:
    units += 1
    result = send_sand(sand_source, cave_map, cave_range, 1)
#show_cave(cave_map, cave_range)
print('Part one:', units)
cave_range[1] += 1
while result != sand_source:
    units += 1
    result = send_sand(sand_source, cave_map, cave_range, 2)
#show_cave(cave_map, cave_range)
print('Part two:', units)

# 23609 too low