import random
def play_game():
        print("Rules of the game: \n"
                    +"Pick R for  rock, P for paper and S for scissors \n"
                    +"Rock vs Paper- paper covers Rock \n"
                    +"Rock vs scissors- Rock smashes Scissors \n"
                    +"Paper vs Scissors- Scissors cuts Paper \n")

        player_choice= input("What is your action?\n R, P or S \n").upper()
        choices=["R", "P", "S"]
        Computer = random.choice(choices)
                
        if player_choice not in choices:
            print("Error, please enter a valid action")
            play_game()

        if player_choice == Computer:  
            print(f'Player {player_choice} : Computer {Computer}')
            print("It's a tie")
            print("Please make another choice")
            play_game()

        elif player_choice == "R":
            if Computer == "S":
                print(f'Player {player_choice}ock : Computer {Computer}cissors')
                print("You win!")
            else:
                print(f'Player {player_choice}ock : Computer {Computer}aper')
                print("Computer wins")

        elif player_choice == "P":
            if Computer == "R":
                print(f'Player {player_choice}aper : Computer {Computer}ock')
                print("You win!")
            else:
                print(f'Player {player_choice}aper : Computer {Computer}cissors')
                print("Computer wins")

        elif player_choice == "S":
            if Computer == "P":
                print(f'Player {player_choice}cissors : Computer {Computer}aper')
                print("You win!")
            else:
                print(f'Player {player_choice}cissors : Computer {Computer}ock')
                print("Computer wins")

play_game()
while True:
    play_again = input("Would you like to  play again? [yes/no]: ")
    if play_again.lower() == "yes":
        play_game()
        continue
    elif play_again =="no":
        print("Thanks for playing :)")
        break
    else:
        print("you have not entered a valid response")
        continue
            
