from src.main_func import *

def parseInput(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split()

def runLoop(lines):
    for line in lines:
        if line[0] == 'BALANCE':
            addBalance(line[1],int(line[2]))
        elif line[0] == 'CHECK_IN':
            checkIn(line[1],line[2],line[3])
        elif line[0] == 'PRINT_SUMMARY':
            printSummary()
        else:
            print('Unknown Command')
    return