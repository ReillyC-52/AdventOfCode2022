import re
Strategy = open("Day_2_input.txt","r")
InputLine = Strategy.readlines()

GameConditionsPart1 = {"X" : [1,{"A":3,"C":6,"B":0}], "Y" : [2,{"B":3,"A":6,"C":0}], "Z" : [3,{"C":3,"A":0,"B":6}]}
# #####PART 1#####
print(f".______      ___      .______     .___________.    __  ")
print(f"|   _  \    /   \     |   _  \    |           |   /_ | ")
print(f"|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`    | | ")
print(f"|   ___/  /  /_\  \   |      /        |  |         | | ")
print(f"|  |     /  _____  \  |  |\  \----.   |  |         | | ")
print(f"| _|    /__/     \__\ | _| `._____|   |__|         |_| ")
TotalVal = 0
for line in InputLine:
    Val1=0
    Val2=0
    line = line.strip()
    Strats = line.split(' ')
    RPS_Pick_Dict = GameConditionsPart1[Strats[1]]
    Val1 = RPS_Pick_Dict[0]
    OutcomeDict = RPS_Pick_Dict[1]
    Val2 = OutcomeDict[Strats[0]]
    TotalVal += Val1 + Val2

print(f'---------------------------------\n')
print(f'PART 1 TOTAL SCORE = {TotalVal}\n')
print(f'---------------------------------\n')

print(f'.______      ___      .______     .___________.    ___   ')
print(f'|   _  \    /   \     |   _  \    |           |   |__ \  ')
print(f'|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`      ) | ')
print(f'|   ___/  /  /_\  \   |      /        |  |          / /  ')
print(f'|  |     /  _____  \  |  |\  \----.   |  |         / /_  ')
print(f'| _|    /__/     \__\ | _| `._____|   |__|        |____|')
 
GameConditionsPart2 = {"X" : [0,{"A":3,"B":1,"C":2}], "Y" : [3,{"A":1,"B":2,"C":3}], "Z" : [6,{"A":2,"B":3,"C":1}]}
TotalVal = 0
for line in InputLine:
    Val1=0
    Val2=0
    line = line.strip()
    Strats = line.split(' ')
    RPS_Pick_Dict = GameConditionsPart2[Strats[1]]
    Val1 = RPS_Pick_Dict[0]
    OutcomeDict = RPS_Pick_Dict[1]
    Val2 = OutcomeDict[Strats[0]]
    TotalVal += Val1 + Val2

print(f'---------------------------------\n')
print(f'PART 2 TOTAL SCORE = {TotalVal}\n')
print(f'---------------------------------\n')
