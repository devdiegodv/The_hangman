from random import choice

words = ['baker', 'dinosaur', 'heliport', 'shark']
correct_letters = []
incorrect_letters = []
tries = 6
successes = 0
game_finished = False

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
    
    return choose_word