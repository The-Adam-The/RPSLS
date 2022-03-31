import random
import time
import sys
import os

from art import art 
from data import moves


sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=100))

while __name__ == "__main__":

    os.system('cls||clear')

    player_move_select = input("""Select your move! 
    1. Scissors 
    2. Paper 
    3. Lizard 
    4. Rock 
    5. Spock.
    """)
    import os
    os.system('cls||clear')
    
    player_move = moves[player_move_select][0]
    cpu_move = random.choice(list(moves[player_move_select][1].keys())) 
    outcome = moves[player_move_select][1][cpu_move]
    

    
    print(f"You chose: {player_move}.")
    time.sleep(1)
    print("\n")
    print("Rock, Spock, Scissors, Lizard, Paper!")
    time.sleep(1)
    print("\n")
    print("Rock, Spock, Scissors, Lizard, Paper!")
    time.sleep(1)
    print("\n")
    print("Rock, Spock, Scissors, Lizard, Paper!")
    time.sleep(1)
    print("\n")

    print(f"You chose: {player_move}.")
    print(f"Your opponent chose: {cpu_move}")
    
    print("\n")

    print(outcome[1])

    if outcome[0]:
        print(art[str(player_move)])
    else:
        print(art[str(cpu_move)])

    play_again = input("Play again? y/n")
    if play_again == "n":
        quit()
    
    print("\n")

