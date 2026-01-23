import math

def positionBounding(currentPosition):
    
    if currentPosition < 0:
        currentPosition += 100
    elif currentPosition > 99:
        currentPosition -= 100
    
    return currentPosition

def longInst(value,currentPosition,count):
    
    currentPosition += value

    interimValue = currentPosition - (currentPosition % 100)
    rotation = abs(math.floor((interimValue) / 100))
    
    count += rotation
    currentPosition %= 100
    currentPosition = positionBounding(currentPosition)

    return currentPosition,count

test = False
if test:
    source = './adventOfCode/2025/Day1/testInputCodeD1.txt'
else:
    source = './adventOfCode/2025/Day1/inputCodeD1.txt'
list1 = []

with open(source,'r') as file:
    for line in file:
        line = line.strip()
        list1.append(line)

direction = ''
value = 0
currentPosition = 50
count = 0
previousDirection = ''
previousPosition = currentPosition
countExeceptions = 0
countExeceptions2 = 0
part1Count = 0

for x in list1:
    direction = x[0]
    value = int(x[1:])

    if direction == 'L':
        value *= -1
    
    output = longInst(value,currentPosition,count)

    currentPosition = output[0]
    count = output[1]

    if direction == 'R' and previousDirection == 'L' and previousPosition == 0:
        count += 1
        countExeceptions += 1

    if direction == 'L' and previousDirection =='R' and previousPosition == 0:
        count -= 1
        countExeceptions2 += 1

    if currentPosition == 0:
        part1Count += 1

    previousDirection = direction
    previousPosition = currentPosition

print(f'answer: {count}, exception1: {countExeceptions}, exception2: {countExeceptions2}, Zeros: {part1Count}, final position: {currentPosition}')
