import re
IDPairs = open("Day_4_input.txt","r")
InputLine = IDPairs.readlines()

# #####PART 1#####
print(f".______      ___      .______     .___________.    __  ")
print(f"|   _  \    /   \     |   _  \    |           |   /_ | ")
print(f"|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`    | | ")
print(f"|   ___/  /  /_\  \   |      /        |  |         | | ")
print(f"|  |     /  _____  \  |  |\  \----.   |  |         | | ")
print(f"| _|    /__/     \__\ | _| `._____|   |__|         |_| ")
TotalPairs = 0
Dict = {}
for line in InputLine:
    line = line.strip()
    Ranges = line.split(',')
    for count in range(len(Ranges)):
        Dict[count] = Ranges[count].split('-')
    if int(Dict[0][0]) > int(Dict[1][0]): 
        if int(Dict[0][1]) <= int(Dict[1][1]):
            TotalPairs+=1
    elif int(Dict[0][0]) < int(Dict[1][0]): 
        if int(Dict[1][1]) <= int(Dict[0][1]):
            TotalPairs+=1
    else:
        TotalPairs+=1
print(f'---------------------------------\n')
print(f'PART 1 TOTAL SCORE = {TotalPairs}\n')
print(f'---------------------------------\n')

print(f'.______      ___      .______     .___________.    ___   ')
print(f'|   _  \    /   \     |   _  \    |           |   |__ \  ')
print(f'|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`      ) | ')
print(f'|   ___/  /  /_\  \   |      /        |  |          / /  ')
print(f'|  |     /  _____  \  |  |\  \----.   |  |         / /_  ')
print(f'| _|    /__/     \__\ | _| `._____|   |__|        |____|')
TotalOverlaps = 0
Dict = {}
for line in InputLine:
    line = line.strip()
    Ranges = line.split(',')
    CheckList = []
    for count in range(len(Ranges)):
        Dict[count] = list(map(int,Ranges[count].split('-')))

    if (Dict[0][1] - Dict[0][0]) > (Dict[1][1] - Dict[1][0]):
        for x in range(Dict[0][0],Dict[0][1]+1):
            CheckList.append(x)
        if Dict[1][0] in CheckList or Dict[1][1] in CheckList:
            TotalOverlaps+=1
    else:
        for x in range(Dict[1][0],Dict[1][1]+1):
            CheckList.append(x)
        if Dict[0][0] in CheckList or Dict[0][1] in CheckList:
            TotalOverlaps+=1
print(f'---------------------------------\n')
print(f'PART 2 TOTAL SCORE = {TotalOverlaps}\n')
print(f'---------------------------------\n')
