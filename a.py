game_list = [0, 1, 2]

def display_game(game_list):
    print(f"here is the current list: {game_list}")
    


def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input('pick a choice in (0, 1, 2): ')
        if choice not in ['0', '1', '2']:
            print("sorry invalid choice!")

    return int(choice)
    
def replacement_choice(game_list, position):
    user_placements = input("type a string for the position")
    game_list[position] = user_placements
    return game_list
    
def gameon_choice(game_list):
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input('pick a choice in (Y, N): ')
        if choice not in ['Y', 'N']:
            print("sorry invalid choice!")

    if(choice == 'Y'):
        return True
    else:
        print(f'so the final updated list till now is {display_game(game_list)}')
        return False
        
game_on = True
game_list = [0, 1, 2]
while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice(game_list)

