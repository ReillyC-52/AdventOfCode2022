import re
Singal = open("Day_6_input.txt","r")
InputLine = Singal.readline()

# #####PART 1#####
print(f".______      ___      .______     .___________.    __  ")
print(f"|   _  \    /   \     |   _  \    |           |   /_ | ")
print(f"|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`    | | ")
print(f"|   ___/  /  /_\  \   |      /        |  |         | | ")
print(f"|  |     /  _____  \  |  |\  \----.   |  |         | | ")
print(f"| _|    /__/     \__\ | _| `._____|   |__|         |_| ")
charCount = markerFlag = 0
charList = [x for x in InputLine]
markerList = []

def checkForMarker(list):
    unique = []
    for char in list:
        if char not in unique:
            unique.append(char)
        else:
            return 0
    return 1

for char in charList:
    if not markerFlag:
        if len(markerList) > 3:
            charCount+=1
            markerList.pop(0)
            markerList.append(char)
            markerFlag = checkForMarker(markerList)
        else:
            charCount+=1
            markerList.append(char)
            if len(markerList) == 4:
                markerFlag = checkForMarker(markerList)
    else: 
        break
print(f'---------------------------------\n')
print(f'PART 1 MARKER LOCATION = {charCount} \n')
print(f'---------------------------------\n')

# print(f'.______      ___      .______     .___________.    ___   ')
# print(f'|   _  \    /   \     |   _  \    |           |   |__ \  ')
# print(f'|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`      ) | ')
# print(f'|   ___/  /  /_\  \   |      /        |  |          / /  ')
# print(f'|  |     /  _____  \  |  |\  \----.   |  |         / /_  ')
# print(f'| _|    /__/     \__\ | _| `._____|   |__|        |____|')

charCount = markerFlag = 0
charList = [x for x in InputLine]
markerList = []
for char in charList:
    if not markerFlag:
        if len(markerList) > 13:
            charCount+=1
            markerList.pop(0)
            markerList.append(char)
            markerFlag = checkForMarker(markerList)
        else:
            charCount+=1
            markerList.append(char)
            if len(markerList) == 14:
                markerFlag = checkForMarker(markerList)
    else: 
        break
print(f'---------------------------------\n')
print(f'PART 2 MARKER LOCATION = {charCount} \n')
print(f'---------------------------------\n')
