from ascii_art import *


def show_menu():
    print(hangman_man, hangman)

    print("")
    print("HOW TO PLAY:")
    print("")
    print(" Try to figure out the secret word by guessing letters. \n For every wrong letter, a limb is removed from the hanging man. \n If you guess the word in less than six attempts you win, \n otherwise you run out of lives and lose the game.")
    print("-----------------------------------------------")
    print("")
    print(" LEVEL OF DIFFICULTY:")
    print("")
    print(" -----------------------------------------------")
    print(" |1.   EASY    |2.  MEDIUM   |3.    HARD        ")
    print(" -----------------------------------------------")
    print("")


def exit_game():
    print(end_message)
    quit()


# Word lists
easy_level = [
    "advice", "accent", "appreciate", "banner",
              "birthday", "beneficiary", "chance", "countryside", "dentist",
              "trouser", "shadow", "power", "monster", "folklore", "eject",
              "guitar", "joke", "Kangaroo"
]

medium_level = [
    "funny", "bunny", "bomb", "mock", "muck",
    "lucky", "ducky", "faux", "stuff", "dump", "void", "skunk", "galaxy"
]


hard_level = [
    "abyss", "axiom", "azure", "affix", "bayou", "buxom",
    "buckaroo", "buffoon", "bagpipes", "buzzwords", "curacao", "dwarves" "disavow", "espionage",
    "embezzle", "fuchsia", "galvanize", "haphazard", "iatrogenic", "jazz", "razzmatazz", "triphthong", "xylophone",
    "voyeurism"
]
