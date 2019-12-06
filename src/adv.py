from room import Room
from player import Player
from item import Item

# Declare all items

item = {
    'dagger': Item('dagger', 'rusty'),
    'shovel': Item('shovel', 'old'),
    'gold': Item('gold', 'shiny'),
    'ring': Item('ring'),
    'carcus': Item('carcus'),
    'ore': Item('ore'),
    'cloak': Item('cloak', 'withered moth eaten cloack'),
    'turnips': Item('turnips', 'looks moldy')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [item['dagger'], item['shovel'], item['gold']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['ring'], item['carcus']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['ore']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['cloak']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['turnips']]),
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

# return new room for player
def new_room(current_room, cmd):
    if cmd == 'n':
       return current_room.n_to
    elif cmd == 's':
       return current_room.s_to
    elif cmd == 'e':
       return current_room.e_to
    elif cmd == 'w':
       return current_room.w_to

#
# Main
#
def main():
    player = Player("Talls", room['outside'])
    while True:
        current_room = player.current_room
        print(f'\n{player.current_room.name}')
        print(f'\n{player.current_room.description}')
        print(f'\nThe following is available in the room: {player.current_room.items}. What would you like?')
        cmd = input("What now?: ")

        parsed_cmd = cmd.split()

        if (len(parsed_cmd) == 2):
            action_word = parsed_cmd[0]
            item_word = parsed_cmd[1]
            
            if (action_word== 'get' or action_word == 'take'):
                print(f'trying to {action_word} {item_word}')
                for item in player.current_room.items:
                    print(f'{item_word}')
                    print(f'{item}')
                    if item.name == item_word:
                        player.add_item(item)
                        current_room.remove_item(item)
                        item.on_take(item)
                        # print(f'player inventory: {player.inventory}')

            elif (action_word == 'drop' or action_word == 'remove'):
                for item in player.inventory:
                    if item.name == item_word:
                        player.remove_item(item)
                        current_room.add_item(item)
                        item.on_drop(item)
                # print(f'trying to {action_word} {item_word}')


        elif (len(parsed_cmd) == 1):
            if cmd == 'q':
                print('Player quit. Game over!')
                break
        
            elif cmd == 'i' or cmd == 'inventory':
                print(f'Your inventory: {player.inventory}')
                continue

            elif cmd not in ['n', 's', 'e', 'w']:
                print('Please provide a valid command.')
                continue

            
            potential_room = new_room(current_room, cmd)

            if (potential_room):
                player.current_room = potential_room
            else:
                print('***No room in that direction***')

        else:
            print('Please try one command at a time.')        

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
