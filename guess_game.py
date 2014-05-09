#http://www.codeskulptor.org/#user30_ZtHUwwpsculLKqn.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simpleguitk as simplegui
import random

# initialize global variables used in your code
num_range = 100
secret_number = -1
guess_number = -2
remaining_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number, remaining_guesses

    remaining_guesses = 7    
    secret_number = random.randrange(0,num_range)
    # just printing the commands to user
    if num_range == 100:
        print('New game. range is from 0 to 100')
    elif num_range == 1000:
        print('New game. range is from 0 to 1000')
    print


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    
    num_range = 1000
    new_game()
    
def get_input(string_input):
    global guess_number
    guess_number = int(string_input)
    input_guess()
    
def input_guess():
    global remaining_guesses, secret_number, guess_number
    
    #print 'teste de variavel = '+str(remaining_guesses) 
    if remaining_guesses < 1:
        print 'You ran out of guesses. The number was '+str(secret_number)
        new_game()
    else:
        print 'Guess was '+ str(guess_number)
        remaining_guesses -= 1
        print 'Number of remaining guesses is '+str(remaining_guesses)    
        if guess_number == secret_number:
            print 'Correct!'
            print
            new_game()
        elif guess_number > secret_number:
            print'Lower'
            print
        else:
            print 'Higher'
            print
    
# create frame
f = simplegui.create_frame('Brincadeira da adivinhacao',200,200)

# register event handlers for control elements
f.add_button("Range is [0, 100]", range100,200)
f.add_button('Range is [0, 1000]', range1000, 200)
f.add_input('Enter a guess.',get_input,100)

# call new_game and start frame
f.start
new_game()

""" always remember to check your completed 
program against the grading rubric"""