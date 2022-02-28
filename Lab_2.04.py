'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction: prints a and d                                            
    actual: same as prediction

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: prints 2
    actual: prints c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: error
    actual: e

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: ['a', 'b', 'c', 'haha', 'e']
    actual: same as prediction

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

#prize game code
prizeList=['a trophy', 'a guitar', 'a drum kit', 'a cat', 'a dog', 'a computer', 'an umbrella', 'a warm coat', 'some money', 'nothing',]
prize=int(input("Pick a number between 0 and 9. "))
print(f"You win {prizeList[prize]}!")

3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

------------------------------
My Code
------------------------------
#starter code
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','bagels']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
q1 = input('Do you like food with holes? ')
if q1 == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

#more questions
q2 = input("Do you like animal products? ")
if q2 == 'y':
    score[2] = score[2] + 1
    score[4] = score[4] + 1
q3 = input("Do you like foods with diverse flavors? ")
if q3 == 'y':
    score[0] = score[0] + 1
    score[5] = score[5] + 1
q4 = input("Do you like syrup? ")
if q4 == 'y':
    score[1] = score[1] + 1
    score[3] = score[3] + 1
q5 = input("Do you like foods with many types of preperation? ")
if q5 == 'y':
    score[4] = score[4] + 1
q6 = input("Do you like crispy/crunchy foods? ")
if q6 == 'y':
    score[2] = score[2] + 1
    score[3] = score[3] + 1
q7 = input("Do you like chewy foods? ")
if q7 == 'y':
    score[0] = score[0] + 1
    score[1] = score[1] + 1
    score[4] = score[4] + 1
    score[5] = score[5] + 1
q8 = input("Do you like food? ")
if q8 == 'y':
    score[0] = score[0] + 1
    score[1] = score[1] + 1
    score[2] = score[2] + 1
    score[3] = score[3] + 1
    score[4] = score[4] + 1
    score[5] = score[5] + 1

#results

print(score)
print(food)

fav_food_index = score.index(max(score))

print(f"Your favorite food is {food[fav_food_index]}.")
#I can't get this program to display two foods correctly.
food.pop(fav_food_index)
score.pop(fav_food_index)

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a?
Type in print(a[3][0]).
'''