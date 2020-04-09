from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('love'), Item('ice')]
                     ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# return the items in the room
def room_items(room):
    if len(room.items) is not 0:
        return room.items
    else:
        return None


# return the possible next room
def next_room(current, direction):
    if direction == 'n':
        return current.n_to
    elif direction == 's':
        return current.s_to
    elif direction == 'e':
        return current.e_to
    elif direction == 'w':
        return current.w_to


#
# Main
#

player = Player('Talls', room['outside'])

def main():
    while True:
        current = player.current_room
        print(f"\n{player.name} is in: {current.name}")
        print(f"{current.description}")
        print(f"Items in room: {room_items(current)}")
        cmd = input("What would you like to do next? ")
        print(cmd)

        parsed_cmd = cmd.split()

        if len(parsed_cmd) == 1:
            print('this is working.........')

            if cmd == 'q':
                print(f"Player quit the game.")
                break
            elif cmd == 'i' or cmd == 'inventory':
                print(f"You have the following items: {player.inventory}")
            elif cmd in ['n', 's', 'e', 'w']:
                print(f"we willl figure out next room...hold tight")
                possible_next_room = next_room(current, cmd)

                if possible_next_room is not None:
                    player.current_room = possible_next_room
                    continue # is this necessary?!?
                else:
                    print(f"\nThere is no room in that direction. Try a different direction.")

            else:
                print(f"Please enter a valid direction or command.")

        elif len(parsed_cmd) == 2:
            print('whoaaaaaaaaaaa')
            action = parsed_cmd[0]
            item = parsed_cmd[1]
            
            if action in ['take', 'get']:
                print(f"we got to take {item}")


                for r_item in player.current_room.items:
                    print(f"{r_item} in room")
                    print(f"{item} to be taken")
                    if r_item.name == item:
                        print(f"print statement is workingggggggggggggggggg")
                        player.add_item(r_item)
                        current.remove_item(r_item)
                        r_item.on_take(r_item)

                    # what if the item requested to be taken is not valid


            elif action == 'drop':
                print(f"we got to drop {item}")

                for p_item in player.inventory:
                    if p_item.name == item:
                        print(f"player has to drop {item}")
                        player.remove_item(p_item)
                        current.add_item(p_item)
                        p_item.on_drop(p_item)

                # what if the player does not have that item in their inventory??????

            else:
                print(f"please provide a valid action")

        else:
            print(f"Please enter one acceptable command at a time.")


main()

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
