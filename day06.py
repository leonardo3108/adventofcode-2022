for line in open('input06.txt'):
    pass
packet = line.rstrip()
#print(packet)
for start_position in range(len(packet)-3):
    end_position = start_position + 4
    marker = packet[start_position:end_position]
    check = sorted(marker)
    if check[0] != check[1] and check[1] != check[2] and check[2] != check[3]:
        break
    #else:        print(end_position, marker, 'nok')
print('Part one:', end_position, '(' + marker + ')')
