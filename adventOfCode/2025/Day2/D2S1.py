def validCheck(current):
    
    if current % 2 != 0:
        current
    else:
        current = 0

    return current

def readFile(filename):
    
    list1 = []

    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            line = line.split(',')
            list1.append(line)

    return list1


if __name__ == "__main__":

    source = './adventOfCode/2025/Day2/testInputCodeD2.txt'
    #source = './adventOfCode/2025/Day2/InputCodeD2.txt'

    invalidID = []
    list1 = readFile(source)

    for range in list1:
        range.split()
        start = range[0]
        end = range[-1]

        ID = start
        
        while ID < end:
        
            invalidID.append(validCheck(ID))
            ID += 1

    print(sum(invalidID))


