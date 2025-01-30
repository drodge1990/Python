with open('./fileManipulation/input.txt','r') as file:
    list1 = []
    list2 = []

    for line in file:
        line = line.strip()


ccImp = []

ee = []

for line in list1:
    ee = list1[0]
a = {'<POSTID>':'MAIN','<1120>':None,'<1120R>':None,'<1121>':None,'<1121R>':None,'<1122>':None,'<1122R>':None,'<1250>':None,'<1250R>':None,'<1440>':None,'<1440R>':None}
ee = [*{*ee}]
ccImp = {EMPID: a for EMPID in ee}

for x in list1:
    currEmp = next(item for item in ccImp if item['EMPID'] == x[0])
    if x[8] == 'Standard':
        currEmp['<1120>'] = x[9]
        currEmp['<1120R>'] = x[10]
    elif x[8] == 'Saturday':
        currEmp['<1121>'] = x[9]
        currEmp['<1121R>'] = x[10]
    elif x[8] == 'Sunday':
        currEmp['<1120>'] = x[9]
        currEmp['<1120R>'] = x[10]
    elif x[8] == 'Bank Holiday':
        currEmp['<1250>'] = x[9]
        currEmp['<1250R>'] = x[10]
    elif x[8] == 'Holiday':
        currEmp['<1440>'] = x[9]
        currEmp['<1440R>'] = x[10]