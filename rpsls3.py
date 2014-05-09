# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

Names = ['rock','Spock','paper','lizard','scissors']

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print()

    # print out the message for the player's choice
    print("A escolha do jogador foi "+player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = Names.index(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # print out the message for computer's choice
    print("A escolha do computador foi "+Names[comp_number])
    # compute difference of comp_number and player_number modulo five
    delta = (player_number - comp_number)%5
    # use if/elif/else to determine winner, print winner message
    if delta > 2:
        print("O jogador perdeu")
    elif delta == 0:
        print("Houve empate")
    else:
        print("O jogador ganhou !!!")


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")