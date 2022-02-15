#Text Monster Game

#Map of dungeon
dungeon = [
    ['prize', 'boss monster', 'magic stones', 'sword', 'down-stairs'], 
    ['nothing', 'magic stones', 'down-stairs', 'monster', 'up-stairs'], 
    ['nothing', 'sword', 'up-stairs', 'monster', 'magic stones']]

#player info
inventory = []
current_floor = 2
current_room = 0
location = dungeon[current_floor][current_room]

#game intro
print("Welcome to the Text Monster Game! You have been placed in a dungeon, and you need to find the prize! \n"
"In this game, you can either move left, right, up, down, grab items, fight monsters, or ask for these commands again.")

#game loop
while True:

    #update location
    location = dungeon[current_floor][current_room]

    #describe location to user
    if location == 'nothing':
        print("The room you are in has nothing in it.")
    elif location == 'sword':
        print("The room you are in has a sword in it.")
    elif location == 'up-stairs':
        print("The room you are in has stairs leading up.")
    elif location == 'down-stairs':
        print("The room you are in has stairs leading down.")
    elif location == 'monster':
        print("Oh no! You ran into a monster!")
    elif location == 'magic stones':
        print("It's your lucky day! You ran into some magic stones!")
    elif location == 'boss monster':
        print("You are almost done! You just have this final boss to defeat! You can do it!")
    else:
        print("You defeated the monster! Therefore you earn the final prize! Way to go!")
        break


    #player choices
    player_choices = input("What would you like to do? ")
    print(player_choices)

#going right
    if player_choices == 'right':
        current_room += 1
        if current_room == 5:
            print("There are no more rooms in this direction. ")
            current_room = 4

#going left
    elif player_choices == 'left':
        current_room -=1
        if current_room == -1:
            print("There are no more rooms in this direction. ")
            current_room = 0

#going up
    elif player_choices == 'up':
        current_floor -=1
        if location != 'up-stairs':
            print("You can't go up to the next floor here.")
            current_floor +=1

#going down
    elif player_choices == 'down':
        current_floor +=1
        if location != 'down-stairs':
            print("You can't go down to the next floor here.")
            current_floor -=1

#grabbing items
    elif player_choices == 'grab':
        if location == 'sword' or location == 'magic stones':
            inventory.append(location)
            dungeon[current_floor][current_room] = 'nothing'
        else:
            print("There is nothing to grab in this room!")

#showing inventory
    elif player_choices == 'inventory':
        print(inventory)

#fighting monsters
    elif player_choices == 'fight':
        if location == 'monster':
            if 'sword' in inventory:
               print("What a success! You have successfully killed a monster!")
               dungeon[current_floor][current_room] = 'nothing'
            else:
                print("You can't fight a monster without a sword! You are now dead!") 
                break
        elif location == 'boss monster':
            if len(inventory) <=2:
                print("You can't fight the boss because you don't have enough items! Turn back quickly!")
            inventory.remove(inventory[0]) and inventory.remove(inventory[1])
            dungeon[current_floor][current_room] = 'nothing'
            print("Good job! You have killed the boss monster! Now go left to claim your prize!")
        else:
            print("What are you going to fight in here, the walls?")
