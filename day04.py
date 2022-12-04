pairs = [line.rstrip().split(',') for line in open('input04.txt')]
pairs = [[range1.split('-'), range2.split('-')] for range1, range2 in pairs]
containments = overlaps = 0
for [min1, max1], [min2, max2] in pairs:
    min1, max1, min2, max2 = int(min1), int(max1), int(min2), int(max2)
    assert min1 <= max1
    assert min2 <= max2
    if min1 <= min2 and min2 <= max1 or min1 <= max2 and max2 <= max1 or min2 <= min1 and min1 <= max2 or min2 <= max1 and max1 <= max2:
        #print(min1, max1, 'x', min2, max2)
        overlaps += 1
        if min1 <= min2 and max1 >= max2 or min1 >= min2 and max1 <= max2:
            #print(min1, max1, '><', min2, max2)
            containments += 1
print('Part one:', containments)        
print('Part two:', overlaps)        
