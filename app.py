import random
from ascii_art import *
from show_menu import *


def play_game():
    show_menu()
    level = input("Choose a level: ")

    if level == "1":
        chosen_level = easy_level
    elif level == "2":
        chosen_level = medium_level
    elif level == "3":
        chosen_level = hard_level

    else:
        print("Invalid entry, Try again!")
        exit_game()

    chosen_word = random.choice(chosen_level)
    word_length = len(chosen_word)
    user_lives = 6

    display = []
    for letter in chosen_word:
        display.append("_")
    print(' '.join(display))

    game_over = False
    while not game_over:

        guess = input("Guess a letter: ").lower()

        for item in range(word_length):
            letter = chosen_word[item]
            if letter == guess:
                display[item] = letter
                print(' '.join(display))

        if guess not in chosen_word:
            user_lives -= 1
            print(man_stages[user_lives])
            print("You have ", user_lives, "lives left")

            if user_lives == 0:
                game_over = True
                print("You are out of lives! The word was", chosen_word, ".")
                print(end_message)

        if "_" not in display:
            game_over = True
            print("You win!")


while True:
    play_game()
    new_game = input(
        "Would you like to play again? Enter Y for Yes N for No: ").lower()
    if new_game != "y":
        break
        exit_game()
