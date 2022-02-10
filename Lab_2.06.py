'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: Prints a
actual: Prints a on an endless loop

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction: Prints a, which is 1
actual: Keeps adding 1 to a until a reaches 10

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'

Prediction: If the user types in y or n, the program doesn't ask again. If the user types in q or cat, the program asks again.

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''
#Tic-Tac-Toe

#defining variables
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turn_number = 1 #used for loop
player = 1

#print board
print(f"{board[0]} | {board[1]} | {board[2]} \n"
"--------- \n"
f"{board[3]} | {board[4]} | {board[5]} \n"
"--------- \n"
f"{board[6]} | {board[7]} | {board[8]}")

#main loop
while turn_number <=9:
    if player ==1:
        player_symbol = 'X'
    else:
        player_symbol = 'O'
    turn = int(input(f"Pick a spot to place your {player_symbol} on. "))-1
    if turn >= 10 or turn <= -1:
        print("That's not a spot.") #checks if number inputted isn't on board
#replacing spot on board with symbol and printing board
    else:
        board[turn] = player_symbol
        print(f"{board[0]} | {board[1]} | {board[2]} \n"
        "--------- \n"
        f"{board[3]} | {board[4]} | {board[5]} \n"
        "--------- \n"
        f"{board[6]} | {board[7]} | {board[8]}")
        turn_number+=1
        
        if player == 1:
            player = 2
        else:
            player = 1
    
print("Game over!")