import random

words = ['Bake', 'Word', 'List', 'Four', 'Five', 'Nine', 'Good', 'Best', 'Cute', 'Zero', 'Huge', 'Cool', 'Tree', 'Race',
         'Rice', 'Keep', 'Lace', 'Beam', 'Game', 'Mars', 'Tide', 'Ride', 'Hide', 'Exit', 'Hope', 'Cold', 'From', 'Need',
         'Stay', 'Come']
correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0
game_over = False

print()
print("\t\t\t\tWELCOME TO GAME HUB LETS PLAY A GAME--- :)")
print("\t\t\t\tRULES:")
print("\t\t\t\tU WILL HAVE TO ENTER A LETTER TO GUESS A 4 LETTER WORD")
print("\t\t\t\tAND U WILL BE GIVEN 6 LIVES INITIALLY")
print("\t\t\t\tIF U LOSE ALL YOUR SIX LIVES BEFORE GUESSING THE WORD CORRECTLY  U LOSE")
print("\t\t\t\tALL THE BEST!!!!  :)")
print()
print()
name = input("\t\t\t\tPlayer name  ")
print()
print(f"\t\t\t\tHII {name}")


def guess_word(words):
    chosen_word = random.choice(words)
    length_chosen_word = len(chosen_word)
    return chosen_word, length_chosen_word

def ask_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while not is_valid:
        chosen_letter = input("Please choose a letter: ")
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You haven't chosen a correct letter")
    return chosen_letter

def show_new_board(chosen_word):
    hidden_list = []
    for l in chosen_word:
        if l in correct_letters:
            hidden_list.appned(l)
        else:
            hidden_list.append("-")
    print(" ".join(hidden_list))

def check_letter(chosen_letter,hidden_word, tries, matches):
    end = False
    if chosen_letter in hidden_word and chosen_letter in correct_letters:
        correct_letters.append(chosen_letter)
        matches += 1
    elif chosen_letter in hidden_word and chosen_letter in correct_letters:
        print("You have entered the same letter. Try a different letter")
    else:
        incorrect_letters.append(chosen_letter)
        tries-=1

    if tries==0:
        end = lose()
    elif matches == unique_letters:
        end = win(hidden_word)
    return tries, end, matches

def lose():
    print("You don't have any tries left")
    print("The hidden word was" + word)
    return True

def win(revealed_word):
    show_new_board(revealed_word)
    print("Congratulations, you guessed the word!")
    return True

word, unique_letters = guess_word(words)
while (not game_over):
    print('\n'+'*'*20+'\n')
    show_new_board(word)
    print('\n')
    print('Incorrect letters: '+'-'.join(incorrect_letters))
    print(f'Tries : {tries}')
    print('\n'+'*'*20+'\n')
    letter = ask_letter()
    tries, over, right_answers = check_letter(letter, word, tries, right_answers)
    game_over = over
