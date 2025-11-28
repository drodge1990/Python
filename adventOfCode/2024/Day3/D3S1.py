test = True
if test:
    source = './adventOfCode/2024/Day3/testInputCodeD3.txt'
else:
    source = './adventOfCode/2024/Day3/inputCodeD3.txt'

with open(source,'r') as file:
    list1 = []

    for line in file:
        line = line.strip()
        list1.append(line)

print(list1)