import copy

def split_file(source):

    with open(source) as file:
        content = file.read().strip()
    
    split_data = content.split("\n\n")

    fresh_range = split_data[0].splitlines()
    int_fresh_range = [tuple(map(int, r.split('-'))) for r in fresh_range]

    id_list = split_data[1].splitlines()
    id_list_int = list(map(int,id_list))
    
    return id_list_int, int_fresh_range

def check_fresh(fresh_ranges,value):

    for line in fresh_ranges:
        
        start = line[0]
        end = line[1]

        if value >= start and value <= end:
            return True
    
    return False

def combine_ranges(id_ranges):

    check_ranges = sorted(id_ranges,key=lambda x: x[0])

    combined = [check_ranges[0]]

    for current in check_ranges[1:]:
        last = combined[-1]
        if current[0] <= last[1]:
            combined[-1] = (last[0], max(last[1], current[1]))
        else:
            combined.append(current)

    return combined

def part2(ranges):

    output_value = 0

    for id in ranges:
        output_value += id[-1]-id[0]+1

    return output_value

if __name__ == '__main__':

    test = './adventOfCode/2025/Day5/testInputCodeD5.txt'
    source = './adventOfCode/2025/Day5/inputCodeD5.txt'

    input_data = split_file(source)

    fresh = []
    spoiled = []
    fresh_range = input_data[1]
    id_list = input_data[0]

    fresh_range_part2 = copy.deepcopy(fresh_range)
    
    for ingredient_id in id_list:
        if check_fresh(fresh_range,ingredient_id):
            fresh.append(ingredient_id)
        else:
            spoiled.append(ingredient_id)
    
    unique_ranges = combine_ranges(fresh_range_part2)
    part2_output = part2(unique_ranges)

    print(f'part1: {len(fresh)}, part2: {part2_output}')