'''
############################
Lab 2.05 - Tic-Tac-Toe
############################
In your Notebook
1. Predict what will be printed. Then run the program and confirm
Example 1
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[0:3])
print(a[1:4])

Prediction: First one prints 'a' and 'd', second one prints 'b' and 'e'.
Actual: ['a', 'b', 'c'], ['b', 'c', 'd']

Example 2
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:len(a) - 3])

Prediction: Prints 'b' and 'c'.
Actual: Prints 'b'.

Example 3
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.remove('b')
print(a)
print(b)

Prediction: List a is printed unaltered, and b prints ['a', 'c', 'd', 'e']
Actual: List a prints what I thought b would print, and b prints None.

Example 4
---------
a = ['a', 'b', 'c', 'd', 'e']
a[0] = 'haha'
b = a.pop()
print(a)
print(b)

Prediction: In list a, 'a' is replaced with 'haha', and 'e' is removed and printed.
Actual: print(a): ['haha', 'b', 'c', 'd'], print(b): e

Example 5
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a + ['abc']
print(a)
print(b)

Prediction: print(a) is unaltered list a, print(b) is list a with 'abc' at the end.
Actual: Same as prediction.

Example 6
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.append('f')
print(a)
print(b)

Prediction: print(a) is unaltered list a, print(b) prints out ['a', 'b', 'c', 'd', 'e', 'f']
Actual: print(a) is what I predicted print(b) would be, print(b) is None.


2. In script mode (Type your program below the multi-line comment)
We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect
that.
    Example:
        1 | 2 | 3
        ---------
        4 | 5 | X
        ---------
        7 | 8 | 9
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
'''
#defining the spots on the table
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#tic tac toe table
print(f"{board[0]} | {board[1]} | {board[2]} \n"
"--------- \n"
f"{board[3]} | {board[4]} | {board[5]} \n"
"--------- \n"
f"{board[6]} | {board[7]} | {board[8]}")

#pick spot on table
turn = int(input("Pick a spot to place your marker on. "))-1

#replacing spot with X
if turn >= 10 or turn <= 0:
    print("That's not a spot.")
else:
    board[turn] = 'X'

#showing updated board
print(f"{board[0]} | {board[1]} | {board[2]} \n"
"--------- \n"
f"{board[3]} | {board[4]} | {board[5]} \n"
"--------- \n"
f"{board[6]} | {board[7]} | {board[8]}")