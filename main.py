from room import Room
from character import Enemy
from character import Neutral
from rpginfo import RPGInfo
from item import Item

below_lands = RPGInfo("Below Lands")
below_lands.welcome()
RPGInfo.info()
RPGInfo.author = "ChrisPsicoInge"

print("Interaction commands= talk, fight, run")

kitchen = Room('Kitchen')
kitchen.set_description('A pretty modern kitchen full of "state of the art" artifacts')

ballroom = Room("Ballroom")
ballroom.set_description('A "Tiki Bar" is on a side, a "Cafe Bar" is on the other side, and a huge "Sound Station" is at the end of the room')

dining_room = Room('Dining hall')
dining_room.set_description('A big wooden table is in the middle of the room. Apparently, it has been imposible to get a new one, so you have to get used to it')

gaming_room = Room('Gaming room')
gaming_room.set_description('With a "Car Racing Simulator", a "Virtual Reality Environment", an "Ultra-Gaming PC", and a "Console´s Museum", This room will kidnap you forever! Did I mention that it has also a little bar and snack area?')

print("There are " + str(Room.number_of_rooms) + " rooms to explore")

kitchen.link_room(dining_room, "south")
kitchen.link_room(gaming_room, "east")
dining_room.link_room(ballroom,"east")
dining_room.link_room(kitchen,"north")
ballroom.link_room(gaming_room, "north")
ballroom.link_room(dining_room, "west")
gaming_room.link_room(kitchen, "west")
gaming_room.link_room(ballroom, "south")

z001 = Enemy("z001 ", "A skinny zombie")
z001.set_conversation("I advice you get out of the below lands human. You are all the same, thinking that they're alone in this world, but...     ...that's never been truth")
z001.set_weakness("Magic Axe")
dining_room.set_character(z001)

p000 = Neutral("p000 ", "An old zombie")
p000.set_conversation("Thanks for visiting us human, we do not usually have many people visiting us. However I need to advice you to leave, there are many of us who have not healed the wounds of their past lives")
gaming_room.set_character(p000)

mag_axe = Item("Magic Axe")
mag_axe.set_description("An enchanted axe usefull for killing strong enemies")
ballroom.set_item(mag_axe)

sword = Item("Sword")
sword.set_description("A steel sword effective for killing humans")
gaming_room.set_item(sword)

current_room = ballroom
backpack=[]

dead = False
while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input(">")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("Choose your weapon you dirty son of a b****")
            fight_with = input("Magic Axe/Sword")
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    print("You won the battle, but just started a war...")
                    print("cof* cof*")
                    print("Zombie dies*")
                    current_room.set_character(None)
                    print("You won, but at what cost?")
                    dead = True
                else:
                    print("You lost because of the weight of your specie, dirty animal!")
                    print("A sword went through your neck*")
                    print("You start bleeding*")
                    print("GAME OVER")
                    dead = True
            else:
                print("There is no " + fight_with + " in your backpack")
        else:
            print("There is no one here to fight with")
        
    elif command == "run":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("Do not run")
                print("A sword went through your neck*")
                print("You start bleeding*")
                print("You die*")
            else:
                inhabitant.run()
        else:
            print("There is the chance to run out of the house, yo took it...")
    
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
            
RPGInfo.credits()   
