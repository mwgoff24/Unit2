'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
              
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction: true                    Actual: true
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction: false                   Actual: false
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction: true                    Actual: true
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction: true            Actual: false

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. 
Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. 
If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. 
Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. 
Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y

not(x and y) == not x or not y
'''
#Answers
'''
These expressions are the same because the word 'not' just brings the opposite. Some examples are if it is not good, it is bad, and if it is not alive, it's dead.
This principle can be applied to the expressions. 
If it isn't just one variable that makes it true, then it has to be both variables to be true.
If it isn't both variables that make it true, then it has to be one variable or the other to be true.
'''

#Can I Be President?
'''
age = input("How old are you? ")
resident = input("How many years have you lived in the US? ")
natural = input("Are you a natural born ciizen? Type 1 for yes or type 2 for no. ")
print(int(age) >=35 and int(resident) >=14 and int(natural) == 1)
'''
#I Can't Be President?
'''
age = input("How old are you? ")
resident = input("How many years have you lived in the US? ")
natural = input("Are you a natural born ciizen? Type 1 for yes or type 2 for no. ")
print(int(age) <=35 and int(resident) <=14 and int(natural) == 2)
'''
#Can I Ride The Roller Coaster?
'''
height=input("How tall are you in inches? ")
age=input("How old are you? ")
money=input("How many quarters do you have? ")
riderpass=input("Do you have a frequent rider pass? Type 1 for yes or type 2 for no. ")
print((int(money)>=4 or int(riderpass)==1) and (int(age)>=18 or int(height)>=50))
'''