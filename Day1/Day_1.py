import re
Calories = open("Day_1_input.txt","r")
InputLine = Calories.readlines()
ElfCount = 1
ElfCals = 0
ElfMaxCals = [0,0]
#####PART 1#####
print(f".______      ___      .______     .___________.    __  ")
print(f"|   _  \    /   \     |   _  \    |           |   /_ | ")
print(f"|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`    | | ")
print(f"|   ___/  /  /_\  \   |      /        |  |         | | ")
print(f"|  |     /  _____  \  |  |\  \----.   |  |         | | ")
print(f"| _|    /__/     \__\ | _| `._____|   |__|         |_| ")

for line in InputLine:
    if re.search(r'\d',line):
        ElfCals += int(line)
    else:
        if ElfCals > ElfMaxCals[1]:
            ElfMaxCals = [int(ElfCount),int(ElfCals)]
        ElfCount +=1
        ElfCals = 0

print(f' THE ELF WITH THE MOST CALS NEEDED IS #{ElfMaxCals[0]}\n')
print(f' THIS BOI NEEDS {ElfMaxCals[1]} CALORIES LIKE DAWG WTH \n')

#####PART 2#####
print(f'.______      ___      .______     .___________.    ___   ')
print(f'|   _  \    /   \     |   _  \    |           |   |__ \  ')
print(f'|  |_)  |  /  ^  \    |  |_)  |   `---|  |----`      ) | ')
print(f'|   ___/  /  /_\  \   |      /        |  |          / /  ')
print(f'|  |     /  _____  \  |  |\  \----.   |  |         / /_  ')
print(f'| _|    /__/     \__\ | _| `._____|   |__|        |____|')
ElfCount = 1
ElfCals = 0
ElfMaxCals2 = {}
for line in InputLine:
    if re.search(r'\d',line):
        ElfCals += int(line)
    else:
        ElfMaxCals2[ElfCount] = ElfCals
        ElfCount +=1
        ElfCals = 0

res = {key: val for key, val in sorted(ElfMaxCals2.items(), key = lambda ele: ele[1])}
Total = 0
print(f' TOP 3 ELVES : \n')
ElfCount = 1
for x in list(reversed(list(res)))[0:3]:
    print(f' {ElfCount}: ELF #{x} -> TOTAL CALORIES {res[x]}\n')
    ElfCount += 1
    Total += res[x]

print(f' TOTAL OF TOP 3 ELVES -> {Total}\n')



