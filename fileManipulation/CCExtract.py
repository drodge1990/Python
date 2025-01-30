# with open('./fileManipulation/input.txt','r') as file:
#     list1 = []
#     list2 = []

#     for line in file:
#         line = line.strip()
import csv

ccOut = csv.DictReader(open('./fileManipulation/input.csv','r'))

ccImp = []

a = {'<EMPID>':None,'<POSTID>':'MAIN','<1120>':None,'<1120R>':None,'<1121>':None,'<1121R>':None,'<1122>':None,'<1122R>':None,'<1250>':None,'<1250R>':None,'<1440>':None,'<1440R>':None}


for x in ccOut:

    if x['Type'] == 'Standard':
        ccImp['<EMPID>'] = x['Payroll Number']
        ccImp['<1120>'] = x['Hours']
        ccImp['<1120R>'] = x['Rate']
    elif x['Type'] == 'Saturday':
        ccImp['<EMPID>'] = x['Payroll Number']
        ccImp['<1121>'] = x['Hours']
        ccImp['<1121R>'] = x['Rate']
    elif x['Type'] == 'Sunday':
        ccImp['<EMPID>'] = x['Payroll Number']
        ccImp['<1120>'] = x['Hours']
        ccImp['<1120R>'] = x['Rate']
    elif x['Type'] in {'Bank Holiday','Special Day 1','Special Day 2'}:
        ccImp['<1250>'] = x['Hours']
        ccImp['<1250R>'] = x['Rate']
    elif x['Type'] in {'Holiday', 'Saturday Holiday', 'Sunday Holiday'}:
        ccImp['<1440>'] = x['Hours']
        ccImp['<1440R>'] = x['Rate']

print(ccImp)

# fields = ['<EMPID>','<POSTID>':'MAIN','<1120>','<1120R>','<1121>','<1121R>','<1122>','<1122R>','<1250>','<1250R>','<1440>','<1440R>']
# dictOutput = csv.DictWriter(open('./fileManipulation/output.csv','w'), fieldnames=fields)
# dictOutput.writerows(ccImp)