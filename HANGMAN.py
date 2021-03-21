import random

choices = 'python', 'java', 'kotlin', 'javascript'
print("H A N G M A N")
while True:
    while True:
        option = input('Type "play" to play the game, "exit" to quit:')
        if option == "exit":
            exit()
        elif option == "play":
            break
    correct_answer = random.choice(choices)
    ciphered_answer = ["-"] * len(correct_answer)
    print("")
    print("".join(ciphered_answer))
    guesses = set()
    lives = 8
    while '-' in ciphered_answer:
        player_input = input("Input a letter: ")
        if player_input in correct_answer and player_input not in guesses:
            j = 0
            for _ in range(correct_answer.count(player_input)):
                ciphered_answer[correct_answer.index(player_input, j)] = player_input
                j += correct_answer.index(player_input, j) + 1
            print("\n" + "".join(ciphered_answer))
            guesses.add(player_input)
        elif player_input in guesses:
            print("You've already guessed this letter")
            print("\n" + "".join(ciphered_answer))
        elif len(player_input) != 1:
            print("You should input a single letter")
            print("\n" + "".join(ciphered_answer))
        elif player_input not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a lowercase English letter")
            print("\n" + "".join(ciphered_answer))
        else:
            print("That letter doesn't appear in the word")
            lives -= 1
            guesses.add(player_input)
            if not lives:
                break
            print("\n" + "".join(ciphered_answer))
    print("You guessed the word!\nYou survived!\n" if "-" not in ciphered_answer else "You lost!\n")
