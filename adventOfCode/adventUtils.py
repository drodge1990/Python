def readFile(filename):
    
    list1 = []

    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            line = line.split(',')
            list1.append(line)

    return list1       

def csv_writer (data,path):
    filename = path
    outputFile = open(filename,"w",encoding='UTF-8')
    lines = []
    if not bool(data):
        raise Exception('No data passed to function')
    for a in data:
        lines.append(','.join(map(str,a)))
    filedata = '\n'.join(lines)
    outputFile.write(filedata)

    return outputFile     