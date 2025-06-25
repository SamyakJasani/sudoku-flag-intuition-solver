# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:27:35 2023

@author: samyak
"""

import sys

def quit():
    sys.exit()
    
    
def printBoard(board):
    print("\n")
    print("               |           |")
    print("   -------------------------------------")
    print("   |", board[1], "|", board[2], "|", board[3], "|", board[4], "|", board[5], "|", board[6], "|", board[7], "|", board[8], "|", board[9], "|")
    print("   -------------------------------------")
    print("   |", board[10], "|", board[11], "|", board[12], "|", board[13], "|", board[14], "|", board[15], "|", board[16], "|", board[17], "|", board[18], "|")  
    print("   -------------------------------------")
    print("   |", board[19], "|", board[20], "|", board[21], "|", board[22], "|", board[23], "|", board[24], "|", board[25], "|", board[26], "|", board[27], "|")
    print("-------------------------------------------")
    print("   |", board[28], "|", board[29], "|", board[30], "|", board[31], "|", board[32], "|", board[33], "|", board[34], "|", board[35], "|", board[36], "|")
    print("   -------------------------------------")
    print("   |", board[37], "|", board[38], "|", board[39], "|", board[40], "|", board[41], "|", board[42], "|", board[43], "|", board[44], "|", board[45], "|")
    print("   -------------------------------------")
    print("   |", board[46], "|", board[47], "|", board[48], "|", board[49], "|", board[50], "|", board[51], "|", board[52], "|", board[53], "|", board[54], "|")
    print("-------------------------------------------")
    print("   |", board[55], "|", board[56], "|", board[57], "|", board[58], "|", board[59], "|", board[60], "|", board[61], "|", board[62], "|", board[63], "|")
    print("   -------------------------------------")
    print("   |", board[64], "|", board[65], "|", board[66], "|", board[67], "|", board[68], "|", board[69], "|", board[70], "|", board[71], "|", board[72], "|")
    print("   -------------------------------------")
    print("   |", board[73], "|", board[74], "|", board[75], "|", board[76], "|", board[77], "|", board[78], "|", board[79], "|", board[80], "|", board[81], "|")
    print("-------------------------------------------")
    print("               |           |")
    
    
def unchangeable(position):
    return position in given
        


def notInSquare(number, position):
    for s in squares:
        if position in s:
            for pos in s:
                if board[pos] == number:
                    return False 
            return True 
    

def notInColumn(number, position):
    for col in cols:
        if position in col:
            for pos in col:
                if board[pos] == number:
                    return False 
            return True
    

def notInRow(number, position):
    for row in rows:
        if position in row:
            for pos in row:
                if board[pos] == number:
                    return False 
            return True
    

def generateFlags():
    flags = {1: [], 2: [], 3:  [], 4: [], 
             5: [], 6: [], 7: [],  8: [], 
             9: [], 10: [], 11: [], 12: [],
            13: [], 14: [], 15: [], 16: [],
            17: [], 18: [], 19: [], 20: [],
            21: [], 22: [], 23: [], 24: [],
            25: [], 26: [], 27: [], 28: [],
            29: [], 30: [], 31: [], 32: [],
            33: [], 34: [], 35: [], 36: [],
            37: [], 38: [], 39: [], 40: [],
            41: [], 42: [], 43: [], 44: [],
            45: [], 46: [], 47: [], 48: [],
            49: [], 50: [], 51: [], 52: [],
            53: [], 54: [], 55: [], 56: [],
            57: [], 58: [], 59: [], 60: [],
            61: [], 62: [], 63: [], 64: [],
            65: [], 66: [], 67: [], 68: [],
            69: [], 70: [], 71: [], 72: [],
            73: [], 74: [], 75: [], 76: [],
            77: [], 78: [], 79: [], 80: [],
            81: []}
    for pos in board:
        if unchangeable(pos) or board[pos] != ' ':
            continue
        for num in range(1, 10):
            if notInRow(num, pos) and notInColumn(num, pos) and notInSquare(num, pos) and num not in flags[pos]:
                flags[pos].append(num)
    return flags
                
     
def solveEdgeCases(flags):
    for row in rows:
        all_flags_d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        all_flags_l = []
        for pos in row:
            if board[pos] == " ":
                for flag in flags[pos]:
                    all_flags_l.append(flag)
                    all_flags_d[flag] = pos
        for flag in all_flags_l:
            if all_flags_l.count(flag) == 1:
                board[all_flags_d[flag]] = flag
    
    flags = generateFlags()
    for col in cols:
        all_flags_d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        all_flags_l = []
        for pos in col:
            if board[pos] == " ":
                for flag in flags[pos]:
                    all_flags_l.append(flag)
                    all_flags_d[flag] = pos
        for flag in all_flags_l:
            if all_flags_l.count(flag) == 1:
                board[all_flags_d[flag]] = flag
                
    flags = generateFlags()
    for s in squares:
        all_flags_d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        all_flags_l = []
        for pos in s:
            if board[pos] == " ":
                for flag in flags[pos]:
                    all_flags_l.append(flag)
                    all_flags_d[flag] = pos
        for flag in all_flags_l:
            if all_flags_l.count(flag) == 1:
                board[all_flags_d[flag]] = flag
                
def find_empty_cell():
    for pos in range(1, 82):
        if board[pos] == ' ':
            return pos
    return None

def is_safe(pos, num):
    return notInRow(num, pos) and notInColumn(num, pos) and notInSquare(num, pos)

def backtrack():
    pos = find_empty_cell()
    if not pos:
        return True  # Solved

    for num in range(1, 10):
        if is_safe(pos, num):
            board[pos] = num
            if backtrack():
                return True
            board[pos] = ' '  # Backtrack

    return False
    
    
board = {1: ' ', 2: 7, 3: ' ', 4: 5, 
         5: 8, 6: 3, 7: ' ',  8: 2, 
         9: ' ', 10: ' ', 11: 5, 12: 9,
        13: 2, 14: ' ', 15: ' ', 16: 3,
        17: ' ', 18: ' ', 19: 3, 20: 4,
        21: ' ', 22: ' ', 23: ' ', 24: 6,
        25: 5, 26: ' ', 27: 7, 28: 7,
        29: 9, 30: 5, 31: ' ', 32: ' ',
        33: ' ', 34: 6, 35: 3, 36: 2,
        37: ' ', 38: ' ', 39: 3, 40: 6,
        41: 9, 42: 7, 43: 1, 44: ' ',
        45: ' ', 46: 6, 47: 8, 48: ' ',
        49: ' ', 50: ' ', 51: 2, 52: 7,
        53: ' ', 54: ' ', 55: 9, 56: 1,
        57: 4, 58: 8, 59: 3, 60: 5,
        61: ' ', 62: 7, 63: 6, 64: ' ',
        65: 3, 66: ' ', 67: 7, 68: ' ',
        69: 1, 70: 4, 71: 9, 72: 5,
        73: 5, 74: 6, 75: 7, 76: 4,
        77: 2, 78: 9, 79: ' ', 80: 1,
        81: 3}


row1 = list(range(1, 10))
row2 = list(range(10, 19))
row3 = list(range(19, 28))
row4 = list(range(28, 37))
row5 = list(range(37, 46))
row6 = list(range(46, 55))
row7 = list(range(55, 64))
row8 = list(range(64, 73))
row9 = list(range(73, 82))
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]


col1 = [1, 10, 19, 28, 37, 46, 55, 64, 73]
col2 = [2, 11, 20, 29, 38, 47, 56, 65, 74]
col3 = [3, 12, 21, 30, 39, 48, 57, 66, 75]
col4 = [4, 13, 22, 31, 40, 49, 58, 67, 76]
col5 = [5, 14, 23, 32, 41, 50, 59, 68, 77]
col6 = [6, 15, 24, 33, 42, 51, 60, 69, 78]
col7 = [7, 16, 25, 34, 43, 52, 61, 70, 79]
col8 = [8, 17, 26, 35, 44, 53, 62, 71, 80]
col9 = [9, 18, 27, 36, 45, 54, 63, 72, 81]
cols = [col1, col2, col3, col4, col5, col6, col7, col8, col9]

s1 = [1, 2, 3, 10, 11, 12, 19, 20, 21]
s2 = [4, 5, 6, 13, 14, 15, 22, 23, 24]
s3 = [7, 8, 9, 16, 17, 18, 25, 26, 27]
s4 = [28, 29, 30, 37, 38, 39, 46, 47, 48]
s5 = [31, 32, 33, 40, 41, 42, 49, 50, 51]
s6 = [34, 35, 36, 43, 44, 45, 52, 53, 54]
s7 = [55, 56, 57, 64, 65, 66, 73, 74, 75]
s8 = [58, 59, 60, 67, 68, 69, 76, 77, 78]
s9 = [61, 62, 63, 70, 71, 72, 79, 80, 81]
squares = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

given = list()
for pos in board:
    if board[pos] != ' ':
        given.append(pos)

printBoard(board)

count = 1
while True:
    prev_board = board.copy()
    flags = generateFlags()
    for pos in flags:
        if len(flags[pos]) == 1:
            board[pos] = flags[pos][0]
    flags = generateFlags()
    solveEdgeCases(flags)
    if prev_board == board:
        print("\n--> Logical solving exhausted. Switching to backtracking...")
        if backtrack():
            print("\n\n               Solved with backtracking:")
            printBoard(board)
        else:
            print("No solution exists.")
        break

    print(f"\n\n_______________Iteration {count}________________")
    print(f"\n           Positions solved: {list(prev_board.values()).count(' ') - list(board.values()).count(' ')}")
    printBoard(board)
    count += 1
    if ' ' not in board.values():
        print("\n\n               Final answer:")
        printBoard(board)
        break