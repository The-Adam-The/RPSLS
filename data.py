moves = {
       "1": ["scissors", {
        "rock": [0, "You lose! Rock crushes scissors!"],
        "spock": [0, "You lose! Spock smashes scissors!"],
        "paper": [1, "You win! Scissors cuts paper!"],
        "lizard": [1, "You win! Scissors decapitates lizard!"],
        "scissors": [2, "It's a draw!"]
       }
       ],
    "2": ["paper", {
        "scissors": [0, "You lose! Scissors cuts paper!"],
        "lizard": [0, "You lose! Lizard eats paper!"],
        "rock": [1, "You win! Paper covers rock!"],
        "spock": [1, "You Win! Paper disproves Spock!"],
         "paper": [2, "It's a draw!"]
        }
    ],
    "3": ["lizard", {
        "scissors": [0, "You lose! Scissors decapitates lizard!"],
        "rock": [0, "You lose! Rock crushes lizard!"],
        "spock": [1, "You win! Lizard poisons Spock!"],
        "paper": [1, "You win! Lizard eats paper!"],
        "lizard": [2, "It's a draw!"] 
        }
    ],
    "4": ["rock", {
        "spock": [0, "You lose! Spock vaporises rock!"],
        "paper": [0, "You lose! Paper covers rock!"],
        "scissors": [1, "You win! Rock crushes scissors!"],
        "lizard": [1, "You win! Rock crushes lizard!"],
        "rock": [2, "It's a draw!"]
        }
    ],
    "5": ["spock", {
        "lizard": [0, "You lose, Lizard poisons Spock!"],
        "paper": [0, "You lose, Paper disproves Spock!"],
        "rock": [1, "You win, Spock vaporises rock!"],
        "scissors": [1, "You win, Spock smashes scissors!"],
        "spock": [2, "It's a draw!"]
    }
    ]
}
