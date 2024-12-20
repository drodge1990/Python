test = False
if test:
    source = './adventOfCode/Day2/testInputCodeD2.txt'
else:
    source = './adventOfCode/Day2/inputCodeD2.txt'

with open(source,'r') as file:
    list1 = []

    for line in file:
        line = line.strip()
        list1.append(line)

output = 0
previous = 0

for u,set in enumerate(list1):
    item = set.split()
    maximum = len(item) - 1
    direction = ''
    for i,current in enumerate(item):
        
        current = int(current)
        
        if i == 0:
            previous = current
            continue
        elif i == 1:
            if current > previous:
                direction = 'P'
            else:
                direction = 'N'

        if current == previous:
            break
        elif abs(current - previous) > 3:
            break
        elif current > previous and direction == 'N':
            break
        elif current < previous and direction == 'P':
            break
        elif i == maximum:
            output += 1
        else:
            previous = current

print(output)