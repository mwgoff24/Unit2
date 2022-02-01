'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: 
The program asks for one's quest. If their input is to seek the holy grail, the program will say to go on.
If they are not seeking the grail, they are asked for the air-speed velocity of an unladen swallow.
If they ask to be more specific, the bridgekeeper won't know. Else, the program says the person was thrown over.

Actual:
Mostly the same, but the program jumps to the question on swallows if you are seeking the holy grail, and any other answer lets you through.

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: 
Whatever color is picked will send back a message related to that color. 
If that color isn't listed, the program returns it doesn't recognize that color.

Actual: 
Same as prediction.

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

#get 3 sides from user
side1=int(input("What is the length of your first side? "))
side2=int(input("What is the length of your second side? "))
side3=int(input("What is the length of your third side? "))

#can it be a triangle
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print(f"The perimeter is {side1+side2+side3}.")

    #is it a right triangle
    if side1**2+side2**2==side3**2:
        print("This is a right triangle.")
    
    #determine if iscocelese, scalene, or equilateral
    if side1==side2 and side2==side3:
        print("This is an equilateral triangle.")
    elif side1==side2 or side3==side2 or side1==side3:
        print("This is an iscoceles triangle.")
    else:
        print("This is a scalene triangle.")
else:
    print("Those inputs don't make a triangle.")

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
#prizes
prize1='a trophy'
prize2='a guitar'
prize3='a drum kit'
prize4='a cat'
prize5='a dog'
prize6='a computer'
prize7='an umbrella'
prize8='a warm coat'
prize9='some money'
prize10='nothing'
#intro to game show
print("In this game show, there are 10 doors numbered 1-10. \n"
"Pick a door, and you may win a prize!")

#ask user for door
answer=input("What number door will you pick? ")

#prize won
if int(answer) == 1:
    print(f"You win: {prize1}!")
elif int(answer) ==2:
    print(f"You win: {prize2}!")
elif int(answer) ==3:
    print(f"You win: {prize3}!")
elif int(answer) ==4:
    print(f"You win: {prize4}!")
elif int(answer) ==5:
    print(f"You win: {prize5}!")
elif int(answer) ==6:
    print(f"You win: {prize6}!")
elif int(answer) ==7:
    print(f"You win: {prize7}!")
elif int(answer) ==8:
    print(f"You win: {prize8}!")
elif int(answer) ==9:
    print(f"You win: {prize9}!")
else:
    print(f"Sorry, but you win {prize10}.")