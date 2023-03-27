import random
import json
import sys
import time
import os

os.system("")


# Method for printing the title
def print_title():
    print("""\033[94m\033[1m
___________.__               ___________                     ___________
\__    ___/|__| ____         \__    ___/____    ____         \__    ___/___   ____
  |    |   |  |/ ___\   ______ |    |  \__  \ _/ ___\   ______ |    | /  _ \_/ __ \ 
  |    |   |  \  \___  /_____/ |    |   / __  \  \___  /_____/ |    |(  <_> )  ___/
  |____|   |__|\___  >         |____|  (____  /\___  >         |____| \____/ \___  >
                   \/                       \/     \/                            \/
    \033[0m""")


# Method for slow printing to the console
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 10)


# Method to print the menu
def print_menu():
    print("Please choose an option: ")
    print("1.) Play a game.\n2.) View Leaderboards.\n3.) Exit\n")


# Method to create a json file if one has not been created yet
def check_for_json_file(file_path):
    if os.path.exists(file_path):
        print()
    else:
        empty_dict = {}
        with open(file_path, "w") as fp:
            # uncomment if you want empty file
            json.dump(empty_dict, fp, indent=4)
        fp.close()


# Method to load info from json file into program
def load_info():
    filename = 'game_log.json'
    with open(filename) as file:
        user_data = json.load(file)
        return user_data


# Method to store info from program into json file
def store_info(data):
    filename = 'game_log.json'
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Method to display the board
def display_board(gameboard, rows, cols):
    for i in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(cols):
            print("", gameboard[i][j], end=" |")
    print("\n+---+---+---+")


# Method to update the board with player and computer marks
def update_board(choice, mark, gameboard):
    if choice == '0,0':
        gameboard[0][0] = mark
    elif choice == '0,1':
        gameboard[0][1] = mark
    elif choice == '0,2':
        gameboard[0][2] = mark
    elif choice == '1,0':
        gameboard[1][0] = mark
    elif choice == '1,1':
        gameboard[1][1] = mark
    elif choice == '1,2':
        gameboard[1][2] = mark
    elif choice == '2,0':
        gameboard[2][0] = mark
    elif choice == '2,1':
        gameboard[2][1] = mark
    elif choice == '2,2':
        gameboard[2][2] = mark
    else:
        print("Else statement in modify_board() function")


# Method to check the winner of the game
def check_winner(gameboard, plr_mark, cpu_mark, player_name, rows, cols):
    # X-axis
    if gameboard[0][0] == plr_mark and gameboard[0][1] == plr_mark and gameboard[0][2] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[0][0] == cpu_mark and gameboard[0][1] == cpu_mark and gameboard[0][2] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    elif gameboard[1][0] == plr_mark and gameboard[1][1] == plr_mark and gameboard[1][2] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[1][0] == cpu_mark and gameboard[1][1] == cpu_mark and gameboard[1][2] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    elif gameboard[2][0] == plr_mark and gameboard[2][1] == plr_mark and gameboard[2][2] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[2][0] == cpu_mark and gameboard[2][1] == cpu_mark and gameboard[2][2] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    # Y-axis
    if gameboard[0][0] == plr_mark and gameboard[1][0] == plr_mark and gameboard[2][0] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[0][0] == cpu_mark and gameboard[1][0] == cpu_mark and gameboard[2][0] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    elif gameboard[0][1] == plr_mark and gameboard[1][1] == plr_mark and gameboard[2][1] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[0][1] == cpu_mark and gameboard[1][1] == cpu_mark and gameboard[2][1] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    elif gameboard[0][2] == plr_mark and gameboard[1][2] == plr_mark and gameboard[2][2] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[0][2] == cpu_mark and gameboard[1][2] == cpu_mark and gameboard[2][2] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    # Diagonal
    if gameboard[0][0] == plr_mark and gameboard[1][1] == plr_mark and gameboard[2][2] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[0][0] == cpu_mark and gameboard[1][1] == cpu_mark and gameboard[2][2] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    elif gameboard[0][2] == plr_mark and gameboard[1][1] == plr_mark and gameboard[2][0] == plr_mark:
        print(f"\033[32m\033[1m{player_name}\033[0m has won!")
        return player_name
    elif gameboard[0][2] == cpu_mark and gameboard[1][1] == cpu_mark and gameboard[2][0] == cpu_mark:
        print("\033[31m\033[1mComputer\033[0m has won!")
        return "Computer"
    return False


#######################   BEGIN PROGRAM   ###############################

# Check for json file, if not present, one will be created
file_path = 'game_log.json'
check_for_json_file(file_path)

# Print welcome message and open to menu
slowprint("Welcome to...\n\n")
time.sleep(0.5)

# Start main logic loop (menu)
while True:
    print_title()
    print_menu()
    option = input("$> ")
    print()

    # Option 1 starts a game
    if option == '1':
        time.sleep(0.5)
        print("Please enter player name: \n")
        player_name = input("n$> ")
        print()

        users = {}
        record = {}
        progress = {}

        choice_list = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']
        gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        rows = 3
        cols = 3

        turn_ctr = 0

        # Load in json data
        data = load_info()

        win, loss, draw = 0, 0, 0
        w, l, d = "Wins", "Losses", "Draws"

        # Check if player exists
        if player_name not in data.keys():
            print(f"Seems you are a first time player!\nWelcome to Tic-Tac-Toe \033[32m\033[1m{player_name}\033[0m.\n")
            data[player_name] = [record, progress]
            data[player_name][0] = {"Wins": 0, "Losses": 0, "Draws": 0}
            data[player_name][1] = {"Unfinished": "None"}
            win, loss, draw = data[player_name][0]["Wins"], data[player_name][0]["Losses"], data[player_name][0][
                "Draws"]
            print(f"RECORD:\n {w:<15}{l:<15}{d:<15}\n  {win:<15} {loss:<15}{draw:<15}\n")
        else:
            slowprint(f"Welcome back \033[32m\033[1m{player_name}\033[0m!\n")
            time.sleep(0.5)
            win, loss, draw = data[player_name][0]["Wins"], data[player_name][0]["Losses"], data[player_name][0][
                "Draws"]
            print(f"RECORD:")
            time.sleep(0.5)
            print(f"{w:<15}{l:<15}{d:<15}\n  {win:<15} {loss:<15}{draw:<15}\n")
            time.sleep(0.75)

            # Check if player has an unfinished game
            if data[player_name][1]["Unfinished"] != "None":
                mark = data[player_name][1]["Unfinished"]["Mark"]
                player_mark = f"\033[32m\033[1m{mark}\033[0m"
                print(f'Your mark is {player_mark}')
                time.sleep(0.5)
                print(f'Your moves: ', end='')
                cpu_mark = ''
                if mark == 'X':
                    cpu_mark = f"\033[31m\033[1mO\033[0m"
                else:
                    cpu_mark = f"\033[31m\033[1mX\033[0m"
                for move in data[player_name][1]["Unfinished"]["Moves"]:
                    update_board(move, player_mark, gameboard)
                    choice_list.remove(move)
                    print(f'{move}, ', end='')
                print()
                print(f'Computer\'s moves: ', end='')
                for move in data[player_name][1]["Unfinished"]["Comp_moves"]:
                    update_board(move, cpu_mark, gameboard)
                    choice_list.remove(move)
                    print(f'{move}, ', end='')
                time.sleep(0.5)
                print()
                slowprint("Loading...\n")
                time.sleep(1)

        # If player does not have an unfinished game, we start one here
        if data[player_name][1]["Unfinished"] == "None":
            slowprint("Loading...\n")
            time.sleep(0.5)

            player_mark = ''
            cpu_mark = ''

            # Create structure in json file for each player
            data[player_name][1] = {"Unfinished": {"Mark": '', "Moves": [], "Comp_moves": []}}

            # Determine the player's mark (X or O)
            while True:
                player_mark = input("Enter the mark ('X' or 'O') you want to play: \n$> ")
                print()
                if player_mark == 'X':
                    player_mark = f"\033[32m\033[1m{player_mark}\033[0m"
                    cpu_mark = f"\033[31m\033[1mO\033[0m"
                    data[player_name][1]["Unfinished"]["Mark"] = "X"
                    print(
                        f"\n\033[32m\033[1m{player_name}\033[0m will be '{player_mark}', and \033[31m\033[1mComputer\033[0m will be '{cpu_mark}'.\n")
                    break
                elif player_mark == 'O':
                    player_mark = f"\033[32m\033[1m{player_mark}\033[0m"
                    cpu_mark = f"\033[31m\033[1mX\033[0m"
                    data[player_name][1]["Unfinished"]["Mark"] = "O"
                    print(
                        f"\n\033[32m\033[1m{player_name}\033[0m will be '{player_mark}', and \033[31m\033[1mComputer\033[0m will be '{cpu_mark}'.\n")
                    break
                else:
                    print("Incorrect option. Try again.\n")
                    continue

            coin_toss = ''
            coin_options = ['H', 'T']

            # Decide who starts game with coin toss
            while True:
                coin_toss = input("To start game, enter ‘H’ for Heads or ‘T’ for Tails for a coin toss: \n$> ")
                print()
                if coin_toss == 'H' or coin_toss == 'T':
                    break
                else:
                    print("Incorrect option. Try again.\n")
                    continue

            if random.choice(coin_options) == coin_toss:
                print(f"Coin toss goes to \033[32m\033[1m{player_name}\033[0m")
            else:
                print(f"Coin toss goes to \033[31m\033[1mComputer\033[0m")
                turn_ctr = 1
        running = True
        move_list = []
        comp_move_list = []
        display_board(gameboard, rows, cols)

        # Start main game sequence logic
        while running:
            winner = check_winner(gameboard, player_mark, cpu_mark, player_name, rows, cols)
            if winner == player_name:
                data[player_name][1]["Unfinished"] = "None"
                data[player_name][0]["Wins"] = data[player_name][0]["Wins"] + 1
                break
            if winner == "Computer":
                data[player_name][1]["Unfinished"] = "None"
                data[player_name][0]["Losses"] = data[player_name][0]["Losses"] + 1
                break
            if len(choice_list) == 0:
                data[player_name][1]["Unfinished"] = "None"
                data[player_name][0]["Draws"] = data[player_name][0]["Draws"] + 1
                print("\n\033[33m\033[1mDRAW!\033[0m")
                break
            if turn_ctr % 2 == 0:
                print("\nEnter a move. (Press 'q' to quit)")
                move = input("$> ")
                print()
                if move == 'q':
                    slowprint("Program saved and terminated.\n")
                    break
                if move in choice_list:
                    time.sleep(0.75)
                    update_board(move, player_mark, gameboard)
                    choice_list.remove(move)
                    move_list.append(move)
                    data[player_name][1]["Unfinished"]["Moves"] = move_list
                    display_board(gameboard, rows, cols)
                else:
                    print("Invalid choice.\nPlease try again.\n")
                    continue
                turn_ctr += 1
            else:
                while True:
                    winner = check_winner(gameboard, player_mark, cpu_mark, player_name, rows, cols)
                    if winner == player_name:
                        data[player_name][1]["Unfinished"] = "None"
                        data[player_name][0]["Wins"] = data[player_name][0]["Wins"] + 1
                        break
                    if winner == "Computer":
                        data[player_name][1]["Unfinished"] = "None"
                        data[player_name][0]["Losses"] = data[player_name][0]["Lossess"] + 1
                        break
                    if len(choice_list) == 0:
                        data[player_name][1]["Unfinished"] = "None"
                        data[player_name][0]["Draws"] = data[player_name][0]["Draws"] + 1
                        print("\n\033[33m\033[1mDRAW!\033[0m")
                        break
                    cpu_move = random.choice(choice_list)
                    print("\nComputer choice: ", cpu_move)
                    if cpu_move in choice_list:
                        time.sleep(0.75)
                        update_board(cpu_move, cpu_mark, gameboard)
                        choice_list.remove(cpu_move)
                        comp_move_list.append(cpu_move)
                        data[player_name][1]["Unfinished"]["Comp_moves"] = comp_move_list
                        display_board(gameboard, rows, cols)
                        turn_ctr += 1
                        break
        # Store info when game ends or player quits
        store_info(data)

    # Option 2 takes user to the leaderboards
    elif option == '2':
        data = load_info()
        i = 0
        w, l, d = "Wins", "Losses", "Draws"
        for person in sorted(data.keys()):
            win, loss, draw = data[person][0]["Wins"], data[person][0]["Losses"], data[person][0]["Draws"]
            print(f"\033[32m\033[1m{person:^36}\033[0m\n")
            print(f"{w:<15}{l:<15}{d:<15}\n  {win:<15} {loss:<15}{draw:<15}\n______________________________________\n")
            print()
            i += 1
        while True:
            choice = input("Press 'r' to return.\n$> ")
            if choice == 'r':
                break
            else:
                print("Invalid command! Try again.\n")
                continue
        continue

    # Option 3 exits the application
    elif option == '3':
        print("Application terminated.")
        break
    else:
        print("Invalid command! Try again.\n")
        continue
