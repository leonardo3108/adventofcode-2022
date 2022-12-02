plays = [line.rstrip().split() for line in open('input02.txt')]
value = {'X': 0, 'Y': 1, 'Z': 2, 'A': 0, 'B': 1, 'C': 2}

total_one = total_two = 0
for opponent, second in plays:
    # opponent: A for Rock, B for Paper, and C for Scissors
    # you:      X for Rock, Y for Paper, and Z for Scissors.
    value_you, value_opponent = value[second], value[opponent]
    # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)...
    score = value_you + 1
    # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    if value_you == value_opponent:    #draw
        score += 3
    elif value_you == (value_opponent + 1) % 3:   #you won
        score += 6
    #print(opponent, second, value_opponent, value_you, score, (value_opponent + 1) % 3)

    # Your total score is the sum of your scores for each round.
    total_one += score

    #the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    if second == 'Y':
        value_you = value_opponent
        score = 3
    elif second == 'Z':
        value_you = (value_opponent + 1) % 3
        score = 6
    else:
        value_you = (value_opponent - 1) % 3
        score = 0
    score += value_you + 1
    #print(opponent, second, value_opponent, value_you, score)

    # Your total score is the sum of your scores for each round.
    total_two += score
    
print('Part one:', total_one)
print('Part two:', total_two)