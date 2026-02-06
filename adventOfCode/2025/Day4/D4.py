def read_file(filename):
    
    list1 = []

    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            column = []
            for item in line:
                column.append(item)
            list1.append(column)

    return list1

def item_check(full_array):
    
    count = 0
    row = 0
    col = 0
    reference = []
    change_references = []

    for rows in full_array:
        
        for item in rows:
            reference = [row,col]
            if item == '@' and array_check(reference,full_array):
                count += 1
                print(reference)
                change_references.append(reference)
            col += 1
        row += 1
        col = 0

    amended_array = full_array
    
    for change in change_references:
        amended_array[change[0]][change[1]] = '.'

    return count,amended_array

def array_check(reference,total_array):
    adjacent_count = 0
    row, col = reference[0],reference[1]
    max_row = len(full_array) - 1
    max_col = len(full_array[0]) - 1

    #print(f'max row:{max_row} max_col:{max_col}')
    
    if row != 0:
        #have to check above
        if total_array[row - 1][col] == '@':
            adjacent_count += 1
        if col != 0:
        #have to check diagonal left 
            if total_array[row - 1][col - 1] == '@':
                adjacent_count += 1
        if col != max_col:
        #have to check diagonal right
            if total_array[row - 1][col + 1] == '@':
                adjacent_count += 1
    
    if row != max_row:
        #have to check below
        if total_array[row + 1][col] == '@':
            adjacent_count += 1
        if col != 0:
        #have to check diagonal left 
            if total_array[row + 1][col - 1] == '@':
                adjacent_count += 1
        if col != max_col:
        #have to check diagonal right
            if total_array[row + 1][col + 1] == '@':
                adjacent_count += 1
    
    if col != 0:
        #have to check left 
        if total_array[row][col - 1] == '@':
            adjacent_count += 1

    if col != max_col:
        #have to check right
        if total_array[row][col + 1] == '@':
            adjacent_count += 1

    #print(adjacent_count)

    return adjacent_count < 4

if __name__ == '__main__':

    test = './adventOfCode/2025/Day4/testInputCodeD4.txt'
    source = './adventOfCode/2025/Day4/inputCodeD4.txt'

    full_array = read_file(test)
    output1 = item_check(full_array)
    part1,amended_array = output1[0],output1[1]
    part2 = part1

    while item_check(amended_array)[0] > 0:
        
        output2 = item_check(amended_array)

        part2 += output2[0]
        amended_array = output2[1]
    
    print(part2)