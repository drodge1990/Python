with open('./adventOfCode/Day1/inputCodeD1.txt','r') as file:
    list1 = []
    list2 = []

    for line in file:
        line = line.strip()
        part = line.split()

        list1.append(int(part[0]))
        list2.append(int(part[1]))

similarity = []
list2count = {}

for value in list2:
    if value in list2count:
        list2count[value] += 1
    
    else: 
        list2count[value] = 1

for item in list1:
    similarity.append(item * list2count.get(item,0))

output = sum(similarity)

print(output)