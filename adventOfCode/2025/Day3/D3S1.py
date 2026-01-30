def readFile(filename):
    
    list1 = []

    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            list1.append(str(line))

    return list1

def joltageExtract(battery,length):

    offset = length
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
    joltagePart1 = 0
    joltagePart2 = 0
    part1 = 2
    part2 = 12
    banks = readFile(source)

    for battery in banks:
        joltagePart1 += int(joltageExtract(battery,part1))
        joltagePart2 += int(joltageExtract(battery,part2))

    print((f'Part 1: {joltagePart1} Part 2: {joltagePart2}'))