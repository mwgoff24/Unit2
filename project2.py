#Text Monster Game

#Map of dungeon
dungeon = [
    ['prize', 'boss monster', 'magic stones', 'sword', 'down-stairs'], 
    ['nothing', 'sword', 'down-stairs', 'monster', 'up-stairs'], 
    ['nothing', 'sword', 'up-stairs', 'monster', 'magic stones']]

#player info
inventory = []
current_floor = 2
current_room = 0
location = dungeon[current_floor][current_room]

#game intro
print("Welcome to the Text Monster Game! You have been placed in a dungeon, and you need to find the prize! \n"
"In this game, you can either move left, right, up, down, grab items, fight monsters, view your inventory, or ask for these commands again.")

#game loop
while True:

    #update location
    location = dungeon[current_floor][current_room]

    #describe location to user
    if location == 'nothing':
        print("\n"
        "The room you are in has nothing in it.")
    elif location == 'sword':
        print("\n"
        "The room you are in has a sword in it.")
    elif location == 'up-stairs':
        print("\n"
        "The room you are in has stairs leading up.")
    elif location == 'down-stairs':
        print("\n"
        "The room you are in has stairs leading down.")
    elif location == 'monster':
        print("\n"
        "Oh no! You ran into a monster!")
    elif location == 'magic stones':
        print("\n"
        "It's your lucky day! You ran into some magic stones!")
    elif location == 'boss monster':
        print("\n"
        "You are almost done! You just have this final boss to defeat! You can do it!")
    else:
        print("\n"
        "You can now grab the final prize! Way to go!")


    #player choices
    player_choices = input("What would you like to do? ")

#going right
    if player_choices == 'right':
        current_room +=1
        if current_room == 5:
            print("There are no rooms in this direction. ")
            current_room = 4
        elif location == 'monster':
            print("You can't move past a monster into the next room! It killed you!")
            break

#going left
    elif player_choices == 'left':
        current_room -=1
        if current_room == -1:
            print("There are no rooms in this direction. ")
            current_room = 0
        elif location == 'boss monster':
            print("You need to defeat the boss monster before you claim the prize! It killed you!")
            break

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
            print(f"Here is your inventory: {inventory}")
        elif location == 'prize':
            print("Congratulations! You have won the game!")
            break
        else:
            print("There is nothing to grab in this room but the air!")

#showing inventory
    elif player_choices == 'inventory':
        print(f"Here is your inventory: {inventory}")

#fighting monsters
    elif player_choices == 'fight':
        if location == 'monster':
            if 'sword' in inventory:
               print("What a success! You have successfully killed a monster!")
               dungeon[current_floor][current_room] = 'nothing'
               inventory.remove('sword')
               print(f"Here is your inventory: {inventory}")
            else:
                print("You can't fight a monster without a sword! You are now dead!") 
                break
        elif location == 'boss monster':
            if 'sword' and 'magic stones' in inventory:
                dungeon[current_floor][current_room] = 'nothing'
                print("Good job! You have killed the boss monster! Now go left to claim your prize!")
                inventory.remove('sword')
                inventory.remove('magic stones')
                print(f"Here is your inventory: {inventory}")
            else:
                print("You didn't have the necessary items to fight the boss! You died!")
                break
        else:
            print("What are you going to fight in here, the walls?")

#asking for help
    elif player_choices == 'help':
        print("In this game, you can either move left, right, up, down, grab items, fight monsters, view your inventory, or ask for these commands again.")

    else:
        print("That is not an available command. \n"
        "In this game, you can either move left, right, up, down, grab items, fight monsters, view your inventory, or ask for these commands again.")