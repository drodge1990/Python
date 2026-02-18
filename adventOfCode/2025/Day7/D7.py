def read_file(source):
    with open(source) as file:
        content = file.read()

    content = content.splitlines()
    content = [list(x) for x in content]
    
    for line in content:
        for i,item in enumerate(line):
            if item == '.':
                line[i] = 0
    
    return content

def splitting(dataset,start):
    
    interim = [start.index('S')]
    start[interim[0]] = 1
    output = start
    count = 0
    
    for line in dataset:
        positions = [index for index, value in enumerate(line) if value == '^']
        try:
            for value in positions:
                if value in interim:
                    count += 1
                    output[value - 1] += output[value]
                    output[value +1] += output[value]
                    output[value] = 0
                    interim = [index for index, pos1 in enumerate(output) if pos1 > 0]
        except Exception as error:
            print(error)
            pass

    return count,output

if __name__ == '__main__':

    test = './adventOfCode/2025/Day7/test.txt'
    source = './adventOfCode/2025/Day7/source.txt'

    dataset = read_file(source)
    start = dataset.pop(0)
    output = splitting(dataset,start)

    print(output)