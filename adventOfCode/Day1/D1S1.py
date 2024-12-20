
with open('./adventOfCode/Day1/inputCodeD1.txt','r') as file:
    list1 = []
    list2 = []

    for line in file:
        line = line.strip()
        part = line.split()

        list1.append(int(part[0]))
        list2.append(int(part[1]))

distances = []
output = []
list1.sort()
list2.sort()

for item1,item2 in zip(list1,list2):
    
    value = abs(int(item1)-int(item2))
    distances.append(value)

output = sum(distances)
#print(list1)
#print(list2)
#print(distances)
print(output)