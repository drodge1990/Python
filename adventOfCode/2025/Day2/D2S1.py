import math
import textwrap

def invalid(id):

    lengthId = math.floor(math.log10(abs(id))) + 1
    #mid = int(lengthId/2)
    idStr = str(id)

    for splitValue in range(lengthId,1,-1):
        if (lengthId/splitValue) % 1 == 0:
            chunks = textwrap.wrap(idStr,int(lengthId/splitValue))
            if len(set(chunks)) == 1:
                return id

    #if idStr[0:(mid)] == idStr[mid:]:
        #return id
    
    return 0

def validCheck(current):
    
    if (math.floor(math.log10(abs(current))) + 1) % 2 == 0:
        current = invalid(current)
    else:
        current = 0

    return current

def readFile(filename):
    
    list1 = []

    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            list1.append(line)

    return list1


if __name__ == "__main__":

    #source = './adventOfCode/2025/Day2/testInputCodeD2.txt'
    source = './adventOfCode/2025/Day2/InputCodeD2.txt'
    invalidId = []
    list1 = readFile(source)

    for line in list1:
        rang = line.split(',')
        for pair in rang:
            
            item = pair.split('-')
            start = int(item[0])
            end = int(item[-1])

            for id in range(start,end+1):
                #print (id)
                invalidId.append(invalid(id))

    print(sum(invalidId))


