from math import prod

def read_file(source):
    with open(source) as file:
        content = file.read()

    content = content.splitlines()
    return content

def parsing_dataset(dataset):

    operands = list(dataset.pop().replace(' ',''))
    values = [list(x) for x in dataset]
    output = []

    for func in operands:
        current_operation = []
        
        while True:
            current_number = ''
            for line in values:
                if len(line) == 0:
                    break
                current_number += str(line.pop(0))

            current_number = current_number.strip()
            if current_number == '':
                break
            current_operation.append(int(current_number))

        if func == '*':
            output.append(prod(current_operation))
        else:
            output.append(sum(current_operation))

    return output

if __name__ == '__main__':

    test = './adventOfCode/2025/Day6/testInputCodeD6.txt'
    source = './adventOfCode/2025/Day6/inputCodeD6.txt'

    dataset = read_file(source)

    parsed = parsing_dataset(dataset)

    print(sum(parsed))