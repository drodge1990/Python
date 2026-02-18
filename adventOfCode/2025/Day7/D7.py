def read_file(source):
    with open(source) as file:
        content = file.read()

    content = content.splitlines()
    content = [list(x) for x in content]

    return content

def splitting(dataset,start):
    
    interim = [start.index('S')]
    start[interim[0]] = '|'
    output = start
    count = 0
    #part2 = 0
    #prev_interim = 1

    for line in dataset:
        #part2_interim = 0
        positions = [index for index, value in enumerate(line) if value == '^']
        try:
            for value in positions:
                if value in interim:
                    #part2_interim += 1
                    count += 1
                    output[value] = '.'
                    output[value - 1],output[value +1] = '|','|'
                    interim = [index for index, pos1 in enumerate(output) if pos1 == '|']
        except Exception as error:
            print(error)
            pass

        #part2 += n
        #prev_interim = part2_interim

    return count#,part2

if __name__ == '__main__':

    test = './adventOfCode/2025/Day7/test.txt'
    source = './adventOfCode/2025/Day7/source.txt'

    dataset = read_file(test)
    start = dataset.pop(0)
    output = splitting(dataset,start)

    print(output)