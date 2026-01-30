def readFile(filename):
    
    list1 = []

    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            list1.append(str(line))

    return list1

def joltageExtractPart2(battery):

    offset = 12
    startPosition = 0
    internalPosition = 0
    endPosition = len(battery)-(offset-1)
    batteryList = []
    
    while len(batteryList) < offset:
        currentBattery = '-1'
        for i, jolt in enumerate(battery[startPosition:endPosition],1):
            if int(jolt) > int(currentBattery) and i <= endPosition:
                currentBattery = jolt
                internalPosition = i
        
        batteryList.append(currentBattery)
        startPosition += internalPosition
        endPosition += 1
    
    return ''.join(batteryList)

def joltageExtractPart1(battery):

    battery1 = '0'
    battery1Position = 0
    battery2 = '0'
    
    for i,jolt in enumerate(str(battery)):
        if int(jolt) > int(battery1) and i < (len(battery)-1):
            battery1 = jolt
            battery1Position = i

    battery1Position += 1

    for jolt2 in str(battery)[battery1Position:]:
        if int(jolt2) > int(battery2):
            battery2 = jolt2

    joltageStr = battery1+battery2

    joltage = int(joltageStr)
    
    return joltage


if __name__ == "__main__":

    #source = './adventOfCode/2025/Day3/testInputCodeD3.txt'
    source = './adventOfCode/2025/Day3/InputCodeD3.txt'
    joltageListPart1 = []
    joltageListPart2 = []
    banks = readFile(source)

    for battery in banks:
        joltageListPart1.append(int(joltageExtractPart1(battery)))
    
    for battery in banks:
        joltageListPart2.append(int(joltageExtractPart2(battery)))

    print((f'Part 1: {sum(joltageListPart1)} Part 2: {sum(joltageListPart2)}'))