# Tristan Le 3/05/2024

"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal

import random

TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'

MAX_TRIES = 0

# TODO: select target word at random from TARGET_WORDS


def pick_target_word(words):
    
    with open(words, 'r') as file:
        words = file.readlines()

    # selects the word and removes the '\n' at the end
    target_word = random.choice(words).strip()

    return target_word


def validate_word(guess, valid_words):
    
    # opens file as read only
    with open(valid_words, 'r') as file:
        
        # each line has the '\n' removed from the end
        valid_words = [line.strip() for line in file]

    # checks to see if the word is inside the file
    if guess in valid_words:
        valid = True
    
    # since the word isnt in the file it makes the user write a different word
    else:
        print('Invalid word, please enter a valid 5 letter word.')
        valid = False

    return valid


def display_matching_characters(guess, target_word):
    """Get characters in guess that correspond to characters in the target_word"""
    score = []
    
    for i in range(len(guess)):
        
        if guess[i] == target_word[i]:
            score.append(2)

        elif guess[i] in target_word:
            score.append(1)
        
        else:
            score.append(0)
    
    return score

def restart_game():
    restart = input("Would you like to restart the game? Y/N ").lower()

    if restart == "y":
        MAX_TRIES = 0
        game(MAX_TRIES)
    
    else:
        print("Thanks for playing!")
        exit()


# TODO: repeat for MAX_TRIES valid attempts
def game(MAX_TRIES):

    target_word = pick_target_word(TARGET_WORDS)

    # Remove this for final game
    # print(target_word)

    print("Welcome to Guess My Word. Please enter a valid 5 letter word to begin.")
    print("YOU HAVE 6 GUESSES TO GUESS THE WORD")
    print("X = Correct Placement")
    print("O = Correct Letter, Wrong Place")
    print("_ = Incorrect Letter")

    while MAX_TRIES < 6:
        # (start loop)

        guess = input("Enter guess? ").lower()
        # TODO: ensure guess in VALID_WORDS
        
        # boolean
        validword = validate_word(guess, VALID_WORDS)

        if validword == True:    

            # checks if guess word is same as target word
            if guess == target_word:
                print("Your guess is correct!")
                MAX_TRIES += 1
                print(f"You got the word in {MAX_TRIES} attempt(s)!")
                restart_game()
            
            else:

                # provides clues towards what the correct words is

                clues = display_matching_characters(guess, target_word)
                
                # converts, 2, 1, 0 into X, O, _
                for clue in clues:
                    if clue == 2:
                        print('X', end=' ')
                    elif clue == 1:
                        print('O', end=' ')
                    else:
                        # end=' ' makes all prints be on the same line 
                        print('_', end=' ')
                print()

                MAX_TRIES += 1

        else:
            continue
            # (end loop)

    print(f"The word was {target_word}.")
    print("Game Over")
    restart_game()




game(MAX_TRIES)
