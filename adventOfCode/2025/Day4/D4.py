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

    for rows in full_array:
        
        for item in rows:
            reference = [row,col]
            if item == '@' and array_check(reference,full_array):
                count += 1
                print(reference)
            col += 1
        row += 1
        col = 0
    
    return count

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

    full_array = read_file(source)
    
    print(item_check(full_array))