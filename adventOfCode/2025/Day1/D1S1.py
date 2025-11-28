test = True
if test:
    source = './adventOfCode/2025/Day1/testInputCodeD1.txt'
else:
    source = './adventOfCode/2025/Day1/inputCodeD1.txt'

with open(source,'r') as file:
    list1 = []

    for line in file:
        line = line.strip()
        list1.append(line)