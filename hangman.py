from random import choice

words = ['baker', 'dinosaur', 'heliport', 'shark']
correct_letters = []
incorrect_letters = []
tries = 6
successes = 0
finished_game = False

def choose_word(words_list):
    chosen_word = choice(words_list)
    uniques_letters = len(set(chosen_word))

    return chosen_word, uniques_letters

def request_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnñopqrstuvwxyz'

    while not is_valid:
        chosen_letter = input("Choose a letter: ").lower()
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You have not chosen a correct letter")

    return chosen_letter 

def show_new_board(word_chosen):
    hidden_list = []

    for l in word_chosen:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))

def check_letter(chosen_letter, hidden_word, lifes, coincidences, uniques_letters):
    end = False

    if chosen_letter in hidden_word:
        correct_letters.append(chosen_letter)
        coincidences += 1
    else:
        incorrect_letters.append(chosen_letter)
        lifes -= 1

    if lifes == 0:
        end = lost()
    elif coincidences == uniques_letters:
        end = win(hidden_word)

    return lifes, end, coincidences

def lost():
    print("You have run out of lives")
    print("The hidden word was " + word)

    return True

def win(discovered_word):
    show_new_board(discovered_word)
    print("Congratulations, you have found the word !!!")

    return True

word, uniques_letters = choose_word(words)

while not finished_game:
    print('\n' + '*' * 20 + '\n')
    show_new_board(word)
    print('\n')
    print('Incorrects words: ' + '-'.join(incorrect_letters))
    print(f"Lifes: {tries}")
    print('\n' + '*' * 20 + '\n')
    letter = request_letter()

    tries, finished_game, successes = check_letter(letter, word, tries, successes, uniques_letters) 
