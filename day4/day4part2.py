import math
import functools


def filterEmptyRows(lines):
    return [line for line in lines if line != '']

def pivotBoard(board):
    return [[row[i] for row in board] for i in range(len(board[0]))]

def filterWhiteSpace(lines):
    return list(map(lambda x: x.split(), lines))

def groupIntoFives(lines):
    return [[lines[j] for j in range(5*i, (5*i)+5) ] for i in range(0,len(lines)/5)]

def markItem(board, itemToMark):
    return [[item for item in row if item != itemToMark] for row in board]

def parseBoardToInt(board):
    return [[int(item) for item in row] for row in board]

def hasWon(board):
    return any([len(row) == 0 for row in board])

def anyHasWon(boards):
    return any(map(hasWon, boards))

def markBoards(boards, item):
    return map(lambda x: markItem(x, item), boards)

def flatten(board):
    return [item for row in board for item in row]

def calculateScore(board, number):
    return functools.reduce(lambda x,y: x+y, flatten(board), 0) * number

f = open('input.txt')
lines = f.readlines()
lines = map(lambda x: x.strip('\n'), lines)

numbers = lines[0].split(',')
numbers = [int(number) for number in numbers]

lines = lines[1:]
lines = filterEmptyRows(lines)

lines = filterWhiteSpace(lines)

boards = groupIntoFives(lines)
boards = map(parseBoardToInt, boards)
print(len(boards))
pivotBoards = map(pivotBoard, boards)

for number in numbers:
    print(number)
    boards = markBoards(boards, number)
    pivotBoards = markBoards(pivotBoards, number)
    if anyHasWon(boards):
        print('we have a winner')
        print(map(hasWon, boards))
        if len(boards) != 1:
            while anyHasWon(boards):
                indexToDel = map(hasWon, boards).index(True)
                del boards[indexToDel]
                del pivotBoards[indexToDel]
        else:
            print(boards)
            print(calculateScore(boards[0], number))
            break
    if anyHasWon(pivotBoards):
        print('we have a winner')
        print(map(hasWon, pivotBoards))
        if len(pivotBoards) != 1:
            while anyHasWon(pivotBoards):
                indexToDel = map(hasWon, pivotBoards).index(True)
                del pivotBoards[indexToDel]
                del boards[indexToDel] 
        else:
            print(pivotBoards)
            print(calculateScore(pivotBoards[0], number))
            break

