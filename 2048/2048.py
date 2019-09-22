##//////////////////////////////////////////////////////////////////////////////
## Program: 2048.py
##
## Author: Michael Cooney
## Date: 09/21/19
## Description: A text based game of 2048
##
##//////////////////////////////////////////////////////////////////////////////


## input is always a valid game state in the form of a matrix?
## i.e. there is four rows with four integers each, and each integer is a valid
## number is 2048, except for 0, which denotes an empty space.
## A fifth line with one integer (0,1,2,3) denotes which way to move the board,
## left, up, right, down respectively

## determine what variables are needed:
# list to hold board, int to hold direction, list to hold output

## gather input from user/file
inputBoard = []

for i in range(5):
    x = input()
    inputBoard.append(x)

## check what the fifth line of input is,
## use to determine what to do with other pieces
direction = inputBoard[4]

## update cells so to reflect the shift
# how?  condition decides what loop to use?

if direction == 0:
    ## what happens if it needs to move up?
    ## if two vertical numbers are the same, the one on top is doubled
    ## if a zero is above a non zero, all non zeroes below move up until they hit a non zero,
    ## or until they can't move up any further.

    i = inputBoard[0]
    for j in i:
        if j == inputBoard
    
    for i in inputBoard:
        for j in inputBoard:
            # what to do if they're the same
            if (i != 2) and (j == inputBoard[i+1][j]):
                j *= 2
                
            # what to do if it's a zero

            # all other cases





