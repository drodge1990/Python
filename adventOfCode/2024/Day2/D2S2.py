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

def valid(curr, prev, direction):
    if curr == prev:
        return False
    elif prev == None:
        return False
    elif abs(curr - prev) > 3:
        return False
    elif curr > prev and direction == 'N':
        return False
    elif curr < prev and direction == 'P':
        return False
    return True

def check(item, direction):
    dampener = 0
    previous = None
    previousPrevious = None
    for i,current in enumerate(item):
        current = int(current)
        if i == maximum and dampener == 0:
            return True
        if i == 0:
            previous = current
            continue
        if valid(curr=current,prev=previous,direction=direction):
            if i == maximum:
                return True
            else:
                previousPrevious = previous
                previous = current
        elif i == 1:
            dampener += 1
            continue
        elif valid(curr=current,prev=previousPrevious,direction=direction):
            dampener += 1
            previous = current
            if i == maximum and dampener < 2:
                return True
        else:
            break
        if dampener > 1:
            break
    return False

previous = 0

for u,set in enumerate(list1,1):
    item = set.split()
    maximum = len(item) - 1
    if int(item[0]) - int(item[-1]) < 0:
        direction = 'P'
    else:
        direction = 'N'
    
    if check(item=item, direction=direction):
        output += 1
    elif check(item[::-1], 'P' if direction == 'N' else 'N'):
        output += 1
 
print(output)