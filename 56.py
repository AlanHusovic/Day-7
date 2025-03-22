import random


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


display = ["_"] * len(chosen_word)
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()


    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    print("".join(display))


    if "_" not in display:
        game_over = True
        print("You Win!")
