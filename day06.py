from collections import Counter

for line in open('input06.txt'):
    pass
packet = line.rstrip()
#print(packet)

def find_marker(packet, size):
    for start_position in range(len(packet)):
        end_position = start_position + size
        marker = packet[start_position:end_position]
        assert len(marker) == size
        if Counter(marker).most_common()[0][1] == 1:   #[0] get the most common item, [1] the quantity; if it is 1, every characters are distinct, so it is the marker
            break
    return end_position, marker

position, marker = find_marker(packet, 4)
print('Part one:', position, '(' + marker + ')')
position, marker = find_marker(packet, 14)
print('Part two:', position, '(' + marker + ')')
