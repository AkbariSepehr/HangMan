import random
from words import words
from visual import lives_visual_dict
import string
import time

print('''

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

''')
print("\n created by Sepehr")

time.sleep(10)

name_of_player = input("Enter you name please: ")
print("\nHello "+name_of_player+"! \nWelcome to Hangman")
time.sleep(1)
htp = input("Do you already know how to play? \nrespond with [Y/N]: ").upper()
if htp == "Y":
    time.sleep(0.25)
    print("Okay then, lets play :)")
elif htp == "N":
    print('''
    Hangman is a very easy game to learn!
    these are the steps you have to follow:
    1- choose a letter and type it in to save the mans life.
    2- the game will tell you if the letter is correct.
    3- if it is correct, you can use that guide to geuss other letter of the word, and save the man
    4- if it is wrong, your man will become closer to death...
    5- Good Luck :)
    ''')
    time.sleep(0.25)
    print("Thats it. \nlets play now :)")
    time.sleep(1)

time.sleep(1)

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        time.sleep(0.25)
        print("You have", lives,"lives left ", name_of_player,".")
        time.sleep(0.5)
        print(" \nAnd you have used the letter: ".join(used_letters))
        time.sleep(0.5)

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        time.sleep(0.25)
        print('Current word: ', ' '.join(word_list))
        time.sleep(0.25)

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nThe letter you chose,', user_letter, 'is not in the word.')
                time.sleep(0.25)

        elif user_letter in used_letters:
            print("\nYou have already used that letter"+name_of_player+"! \nGuess another one, we have so many.")
            time.sleep(0.25)

        else:
            print('\nThat is not a valid letter! choose from (a-z) only please')
            time.sleep(0.25)

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('GAME OVER, You lost. The word was: ', word)
        print("better luck next time " + name_of_player + " :)")
        time.sleep(5)
    else:
        print('YAY! You guessed the word correctly!!!')
        print("You have saved a life today, "+name_of_player+" be proud")
        time.sleep(5)


if __name__ == '__main__':
    hangman()
