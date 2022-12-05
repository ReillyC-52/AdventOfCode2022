import re
CrateList = open("Day_5_input.txt","r")
InputLine = CrateList.readlines()
# #####PART 1#####
print(f".______      ___      .______     .___________.    __  ")
print(f"|   _  \    /   \     |   _  \    |           |   /_ | ")
print(f"|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`    | | ")
print(f"|   ___/  /  /_\  \   |      /        |  |         | | ")
print(f"|  |     /  _____  \  |  |\  \----.   |  |         | | ")
print(f"| _|    /__/     \__\ | _| `._____|   |__|         |_| ")
def SetActiveStackDict(lines):
    StackLocationDict = {1:1,2:5,3:9,4:13,5:17,6:21,7:25,8:29,9:33,}
    NewStackDict = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
    lines.pop()
    for line in lines:
        for key,val in StackLocationDict.items():
            BoxLocation = line[val:val+1]
            if re.match(r'[A-Z]',BoxLocation):
                NewStackDict[key].insert(0,BoxLocation)
    return NewStackDict

def MoveBoxStack(ActiveStackDict,count,StackFrom,StackTo):
    for _ in range(count):
        ActiveStackDict[StackTo].append(ActiveStackDict[StackFrom].pop())
    return ActiveStackDict
    
ActiveStackDict = {}
StackBuffer = []
MoveFlag = 0
for line in InputLine:
    if MoveFlag:
        LineNumbers = re.findall(r'[0-9]+',line)
        ActiveStackDict = MoveBoxStack(ActiveStackDict,int(LineNumbers[0]),int(LineNumbers[1]),int(LineNumbers[2]))
    else:
        if re.match(r'^\n$',line):
            ActiveStackDict = SetActiveStackDict(StackBuffer)
            MoveFlag  =1
        else:
            StackBuffer.append(line)

AnswerString = ''
for val in ActiveStackDict.values():
    AnswerString = AnswerString + val[-1]
print(f'---------------------------------\n')
print(f'PART 1 CORRECT SQUENCE = {AnswerString}\n')
print(f'---------------------------------\n')

print(f'.______      ___      .______     .___________.    ___   ')
print(f'|   _  \    /   \     |   _  \    |           |   |__ \  ')
print(f'|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`      ) | ')
print(f'|   ___/  /  /_\  \   |      /        |  |          / /  ')
print(f'|  |     /  _____  \  |  |\  \----.   |  |         / /_  ')
print(f'| _|    /__/     \__\ | _| `._____|   |__|        |____|')

def MoveBoxStackMulti(ActiveStackDict,count,StackFrom,StackTo):
    MultiBuffer = []
    for _ in range(count):
        MultiBuffer.append(ActiveStackDict[StackFrom].pop())
    for _ in range(len(MultiBuffer)):
        ActiveStackDict[StackTo].append(MultiBuffer.pop())
    return ActiveStackDict
    
ActiveStackDict = {}
StackBuffer = []
MoveFlag = 0
for line in InputLine:
    if MoveFlag:
        LineNumbers = re.findall(r'[0-9]+',line)
        ActiveStackDict = MoveBoxStackMulti(ActiveStackDict,int(LineNumbers[0]),int(LineNumbers[1]),int(LineNumbers[2]))
    else:
        if re.match(r'^\n$',line):
            ActiveStackDict = SetActiveStackDict(StackBuffer)
            MoveFlag  =1
        else:
            StackBuffer.append(line)

AnswerString = ''
for val in ActiveStackDict.values():
    AnswerString = AnswerString + val[-1]

print(f'---------------------------------\n')
print(f'PART 2 CORRECT SQUENCE = {AnswerString}\n')
print(f'---------------------------------\n')
