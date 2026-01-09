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
currentPosition = 0

for x in list1:
    direction = ''.join(char for char in x if char.isalpha())
    value = int(''.join(char for char in x if char.isnum()))
    if direction is 'L':
        value = value * (-1)
    
    currentPosition = currentPosition+value
    if currentPosition < 0:
        currentPosition + 100
    elif currentPosition > 99:
        currentPosition -100