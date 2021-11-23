# Programmer: Katie Pell

# This was a practice project to learn Python after having a foundation in C++. It has been updated throughtout my CS career:
# - After taking Programming I, I created this game
# - After taking Programming II, I compartmentalized the program into functions
# Next steps for this project
# - Creating a GUI
# - What happens if you guess a letter that you've already guessed?
# - Could actually have the animation of the guy from the game
# - List of guessed letters printed every time
# - Better formatting
# - Redo now and see how much has changed?


def greet_user(thisname):
    print()
    print(f"Hi, {thisname}! Ready to play Hangman?")  # uses user's name input to greet them
    print()


def find_different_letters(s):  # add only letters, and only if they're not already there
    different_letters = []
    for item in s:
        if item not in different_letters and item != " ":
            different_letters.append(item)

    return different_letters


def create_empty_puzzle(s):
    empty_puzzle = []
    for character in s:  # iterate over all characters in phrase
        if character == " ":  # looks for spaces
            empty_puzzle.append(" / ")  # replaces them with /
        else:  # otherwise, for letters
            empty_puzzle.append("_ ")  # adds an underscore to the empty puzzle
    return empty_puzzle


def list_to_string(thislist):
    string_empty_puzzle = ""
    for item in thislist:
        string_empty_puzzle += item  # create a string out of list
    print(string_empty_puzzle, "\n")


def play_the_game(ansChars, empty_puzzle, answer):
    guessed_letters = []  # holds previously guessed letters (not visible to player)
    wrong_guesses = []  # holds wrong guesses - only visible if not empty
    guess_num = 0

    while guess_num <= 20:  # only allow 21 guesses
        player_guess = input("Guess a letter: ")  # ask player for guess

        if not player_guess.isalpha():
            print("Invalid input! Only letters are allowed. Try again!")
            continue

        if player_guess in guessed_letters:  # check to see if it's been guessed
            print("You already guessed this letter. Try again.")
            print()
            continue

        guessed_letters.append(player_guess)  # add guessed letter to list of letters already guessed

        if player_guess in ansChars:  # if in answer, add to guessed letters
            for item in range(0, len(ansChars)):  # iterate through all characters in answer
                if ansChars[item] == player_guess:  # find the index of where the matching one is in the answer
                    empty_puzzle[item] = player_guess  # make that index of empty puzzle hold the guessed letter
        else:  # if not in answer
            wrong_guesses.append(player_guess)

        if "_ " not in empty_puzzle:  # when done solving
            print(answer)
            print()
            print("You won! Nice job.")
            print()
            break
        list_to_string(empty_puzzle) # print empty_puzzle as a string - unless already done

        if len(wrong_guesses) > 0:  # only if there are wrong guesses already
            print("Wrong: ", end=" ")  # print the wrong guesses a few lines down
        for item in wrong_guesses:  # format the line of incorrect guesses properly
            print(item, end=" ")
        print()  # leave some space for easier reading
        print()
        guess_num += 1  # increment guess # after each guess


def main():
    playInput = "y"  # so it runs initially

    while playInput != "n":  # while the player hasn't said no to playing again...
        # make sure it resets for each round of the game

        print()
        name = input("What's your name? ")  # get input from user

        greet_user(name)  # calls greet function

        # these need to be global so they can be accessed by other functions
        answer = input("Choose a word or phrase as an answer: ")  # ask user for answer as input
        ansChars = list(answer)  # create a list out of the characters in the answer input
        different_letters = []  # create a list of the distinct letters in the answer

        print("\n " * 8)  # print 8 lines so the answer isn't visible!

        find_different_letters(different_letters, ansChars)  # do this with all the letters and symbols in the answer

        empty_puzzle = create_empty_puzzle(ansChars)  # creates puzzle with symbols where needed

        list_to_string(empty_puzzle)  # prints puzzle as string from list of characters

        play_the_game(ansChars, empty_puzzle, answer)

        playInput = input("Would you like to play again? y/n ")


main()