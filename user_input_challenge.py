'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''
#code
name=input("What is your name? ")
age=input("How old will you be turning or have turned this year? ")
year=(2022-int(age)+100)
print(f"{name}, you will turn 100 years old in the year {year}.")
repeat=input("Now enter a number. ")
print(int(repeat)*f"{name}, you will turn 100 years old in the year {year}. \n")