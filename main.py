import random
import time

from art import art 
from data import moves

while __name__ == "__main__":

    player_move_select = input("""Select your move! 
    1. Scissors 
    2. Paper 
    3. Lizard 
    4. Rock 
    5. Spock.
    """)
    
    player_move = moves[player_move_select][0]
    cpu_move = random.choice(list(moves[player_move_select][1].keys())) 

    print(f"player_move: {player_move}")
    print(f"cpu_move: {cpu_move}")

    outcome = moves[player_move_select][1][cpu_move]
    

    
    print(f"You chose: {player_move}.")
    print("\n")
    time.sleep(1)
    print("Rock, Spock, Scissors, Lizard, Paper!")
    time.sleep(1)
    print("Rock, Spock, Scissors, Lizard, Paper!")
    time.sleep(1)
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
    
    print("\n")

