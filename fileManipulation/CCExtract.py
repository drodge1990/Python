with open('./fileManipulation/input.txt','r') as file:
    list1 = {}
    list2 = []

    for line in file:
        line = line.strip()
        part = line.split()
