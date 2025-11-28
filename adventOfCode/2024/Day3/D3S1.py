test = True
if test:
    source = './adventOfCode/2024/Day3/testInputCodeD3.txt'
else:
    source = './adventOfCode/2024/Day3/inputCodeD3.txt'
    
list1 = []

with open(source,'r') as file:

    for line in file:
        line = line.strip()
        list1.append(line)

print(list1)