# RockPaperScissors
Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules by watching this youTube video and on wikipedia.

A brief summary:

If the two players choose the same “character” it’s a tie, and the game repeats. 

Rock crushes Scissors 

Paper covers Rock 

Scissors cuts Paper 

One player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player).

The inbuilt Python module random and its choice method was used.

Instructions:

The game is created in a Pyhton file called main.py. 

A list is created to store all possible options: 

"R" for "rock" 

"P" for "paper" 

"S" for "scissors". 

When the program is run, the user is asked to pick an option between "R", "P" or "S" 

If user input is invalid (not amongst the options), an error is printed and it asks for their input again (it is in a loop). 

The choice function from the inbuilt Python random module is used to make a choice for CPU player(computer). 

Both player's moves are printed in the format: Player (Rock) : CPU (Paper) 

Both player's moves are checked;

If there is a winner, it prints the winner, and the program ends. If it's a tie (the computer and player pick the same move), the game is restarted from asking for user input.
