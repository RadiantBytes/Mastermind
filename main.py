#
# CS 224 Spring 2020
# Programming Assignment 3
#
# This program simulates a game of 'Mastermind'.
# In this game, the computer will generate a pattern
# of four colors (white, orange, red, purple, black, green)
# randomly. The user must guess the correct pattern within
# 10 turns. The program will indicate if the user suceeds in
# guessing a correct position and color, or color alone.
#
# @author: Thomas Lynaugh
# Last Modified: March 10, 2020
#

import random
import string

# A Debug-mode boolean
# 0: create_new_game creates a random pattern
# 1: create_new_game creates a game with default patten W G W O
GRADING = 1

def evalute_guess(CPU_pattern, user_guess):

    # Determine which pegs were guessed correctly

    # This keeps tracks of the black and white pegs
    # A white peg ('w') indicates that a color is correct
    # A black peg ('b') indicates a color and position are both correct
    bw_pegs = ""

    for peg in range(len(CPU_pattern)):
        if user_guess[peg] == CPU_pattern[peg]:
            # Color and position is correct
            bw_pegs += 'b'

        elif CPU_pattern[peg] in user_guess:
            # Color is correct, but not position
            bw_pegs += 'w'

        else:
            # Color is not within the CPU's pattern
            bw_pegs += '_'


    # Ensure black/white pegs are mixed
    l = list(bw_pegs)
    random.shuffle(l)
    bw_pegs = ''.join(l)

    return bw_pegs

def get_guess():

    # Prompt a user for input. Ensure the input is valid
    while True:

        user_guess = input("Enter a guess : ")

        # Change user_guess to CPU_pattern's lowercase/trimmed format
        user_guess = user_guess.lower().replace(' ', '')

        # Check if guess is four characters total
        if len(user_guess) != 4:
            print("Please enter a guess of four colors")
            continue
        # Check if guess is in a string format
        elif user_guess.isalpha() == False:
            print("Please enter a guess of four colors as characters")
            continue

        # Ensure the guess is contains valid characters representing the colors
        for c in user_guess:
            if c not in "bwrgpo":
                print("Please enter a valid color guess as a character (b, g, o, p ,r, or w)")
                break

        else:
            break

    return user_guess

def create_new_game(target = "wgwo"):

    # Keeps track of the computer's current pattern
    CPU_pattern = ""

    if (GRADING):
        print("In GRADING Mode!")
        CPU_pattern = target

    else:
        print("In USER mode!")

        # Determine a completely random pattern
        for i in range(4):

        # This line appends a char representing a color from
        # the provided string 'bwrgpo' randomly
            CPU_pattern += random.choice('bwrgpo')


    return CPU_pattern

# Update the ASCII representation of the game board to reflect user guesses
def update_representation(ascii_board, user_guess, bw_pegs, turn_num):

    temp_list = []

    # Convert ascii_board into a temporary list to update it
    # keepends parameter: Keep the newlines at the end of each string. This
    # will make it easier to convert it back into a string
    temp_list = ascii_board.splitlines(keepends=True)

    # Adjust the necessary line based on turn number
    temp_list[turn_num + 4] = "|" + bw_pegs[0] + bw_pegs[1] + "-----" + user_guess + "-----" + bw_pegs[2] + bw_pegs[3] + "|\n"

    # Convert the list back to a string
    str = ""

    for l in temp_list:
        str += l

    return str

# Build an initial ASCII representation of the game board
def build_representation():

    ascii_board =    "        User      \n"
    ascii_board +=  "  ________________\n"
    ascii_board += " /----------------\\\n"
    ascii_board += "|------------------|\n"

    # Allow for 10 turns total
    for l in range(10):
        ascii_board += "|__-----0000-----__|\n"

    ascii_board += "|------------------|\n"
    ascii_board += " \----------------/\n"
    ascii_board += "  \______________/\n"
    ascii_board +=    "       Computer   \n"

    return ascii_board


def print_board(ascii_board):
    print(ascii_board)


def main():

    # Print welcome screen
    print("Welcome to Mastermind\n\n")
    print("\tThe computer will generate a randomized\n"
        + "\tpattern of four colors (black, white, red,\n"
        + "\tgreen, purple, and orange). To win, you must\n"
        + "\tguess the pattern within 10 turns. Guess the\n"
        + "\tpattern by inputting character values, representing\n"
        + "\teach color (b, w, r, g, p, o).\n\n"
        + "\ta black peg (represented by 'b') means that one of the\n"
        + "\tguessed peg's color and position is correct.\n\n"
        + "\ta white peg (represented by 'w') means that one of the\n"
        + "\tguessed peg's colors has been correctly guessed, but\n"
        + "\tthe position is incorrect.\n\n"
        + "################################\n\n")

    # Keep track of the number of turns
    # Go up to 10 turns
    turn_num = 0;

    CPU_pattern = create_new_game()

    ascii_board = build_representation()

    # DEBUG
    #print("The target is " + CPU_pattern)

    print_board(ascii_board)

    # Get user guesses for 10 turns
    while (turn_num < 10):

        print("################################")
        print("\nTurn " + str(turn_num+1) + "!\n")


        guess = get_guess()

        bw_pegs = evalute_guess(CPU_pattern, guess)

        # Check if the user has won
        if bw_pegs == 'bbbb':
            print("\nYou've won!\n")
            exit(0)

        # Update the board to reflect user guesses
        ascii_board = update_representation(ascii_board, guess, bw_pegs, turn_num)

        print_board(ascii_board)

        turn_num += 1

    # If the user does not win within 10 turns, the computer wins
    print("\nCPU won!\n")

if __name__ == "__main__":
    main()
