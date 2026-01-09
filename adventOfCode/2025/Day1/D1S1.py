import re
import math

test = True
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

for x in list1:
    rotations = 0
    direction = ''.join(char for char in x if char.isalpha())
    regex = '\d+'
    valueList = re.findall(regex,x)
    value = int(valueList[0])
    #print(value)
    if direction == 'L':
        value *= -1
    
    if direction == 'R' and currentPosition == 0 and value < 100:
        count += 1

    if (currentPosition + value)/100 == math.floor(abs(currentPosition + value)/100) and currentPosition + value != 0:
        rotations = -1

    currentPosition += value

    rotations += math.floor(abs(currentPosition)/100)
    
    #print(rotations)

    if currentPosition < 0:
        rotations += 1
        currentPosition += 100*rotations
    if currentPosition > 99:
        currentPosition -= 100*rotations
    
    if currentPosition == 100:
        currentPosition -= 100

    count += rotations

    print(f'Instruction: {x} Position: {currentPosition} Count: {count}')
    #if currentPosition == 0:
     #   count += 1

print(f'answer: {count}')