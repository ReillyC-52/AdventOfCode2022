import string
RuckSackList = open("Day_3_input.txt","r")
InputLine = RuckSackList.readlines()

LetterValues = {}
for index,letter in enumerate(string.ascii_lowercase):
   LetterValues[letter] = index + 1

# #####PART 1#####
print(f".______      ___      .______     .___________.    __  ")
print(f"|   _  \    /   \     |   _  \    |           |   /_ | ")
print(f"|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`    | | ")
print(f"|   ___/  /  /_\  \   |      /        |  |         | | ")
print(f"|  |     /  _____  \  |  |\  \----.   |  |         | | ")
print(f"| _|    /__/     \__\ | _| `._____|   |__|         |_| ")
TotalPrioity = 0
for line in InputLine:
    line = line.strip()
    Sack = [x for x in line]
    CompartmentA = Sack[:len(Sack)//2]
    CompartmentB = Sack[len(Sack)//2:]
    for Item in CompartmentA:
        if Item in CompartmentB:
            if Item.isupper() is True:
                TotalPrioity += LetterValues[Item.lower()] + 26
            else:
                TotalPrioity += LetterValues[Item.lower()] 
            break

print(f'---------------------------------\n')
print(f'PART 1 TOTAL PRIORITY = {TotalPrioity}\n')
print(f'---------------------------------\n')

print(f'.______      ___      .______     .___________.    ___   ')
print(f'|   _  \    /   \     |   _  \    |           |   |__ \  ')
print(f'|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`      ) | ')
print(f'|   ___/  /  /_\  \   |      /        |  |          / /  ')
print(f'|  |     /  _____  \  |  |\  \----.   |  |         / /_  ')
print(f'| _|    /__/     \__\ | _| `._____|   |__|        |____|')
#####PART 2
def ElfBadgeFinder(IncomingLines):
    SackList = []
    for line in IncomingLines:
        Sack = [x for x in line]
        SackList.append(Sack)
    for Item in SackList[0]:
        if Item in SackList[1] and Item in SackList[2]:
            if Item.isupper() is True:
                return LetterValues[Item.lower()] + 26
            else:
                return LetterValues[Item.lower()] 

TotalPrioity = 0
ElfGroupCount = 0
ElfGroupBuffer = []
for line in InputLine:
    line = line.strip()
    if ElfGroupCount > 2:
        Priority = ElfBadgeFinder(ElfGroupBuffer)
        TotalPrioity += Priority
        ElfGroupCount = 0
        ElfGroupBuffer = []
    ElfGroupCount +=1
    ElfGroupBuffer.append(line)

TotalPrioity += ElfBadgeFinder(ElfGroupBuffer)
print(f'---------------------------------\n')
print(f'PART 1 TOTAL PRIORITY = {TotalPrioity}\n')
print(f'---------------------------------\n')

