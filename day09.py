#moves = [(direction, int(quantity)) for direction, quantity in [line.rstrip().split() for line in open('input09.t[0]t')]]
directions = ''.join([direction * int(quantity) for direction, quantity in [line.rstrip().split() for line in open('input09.txt')]])
moves = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}

def process(directions, moves, quantity_knots):
    knots = [[0, 0] for _ in range(quantity_knots)]
    passings = {}

    for direction in directions:
        assert direction in moves
        for dim in [0, 1]: knots[0][dim] += moves[direction][dim]
        for index in range(1, len(knots)):
            t = knots[index]
            h = knots[index - 1]
            if t[0] not in [h[0] - 1, h[0], h[0] + 1] or t[1] not in [h[1] - 1, h[1], h[1] + 1]:
                if t[0] > h[0]:
                    t[0] -= 1
                elif t[0] < h[0]:
                    t[0] += 1
                if t[1] > h[1]:
                    t[1] -= 1
                elif t[1] < h[1]:
                    t[1] += 1
        if tuple(t) in passings:
            passings[tuple(t)] = passings[tuple(t)] + 1
        else:
            passings[tuple(t)] = 1
    return passings

passings = process(directions, moves, 2)
print('Part one:', len(passings.keys()))

passings = process(directions, moves, 10)
print('Part one:', len(passings.keys()))

