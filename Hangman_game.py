import random
import hangman_stages
import world_file

lives = 6
chosen_world = random.choice(world_file.words)
display = []
for i in range(len(chosen_world)):
    display += "_"
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_world)):
        letter = chosen_world[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_world:
        if guessed_letter not in chosen_world:
            lives -=1
            if lives == 0:
                game_over = True
                print("You lose!!")
                print(f"The word was '{chosen_world}'.")
    if '_' not in display:
        game_over = True
        print("You won!!")
    print(hangman_stages.stages[lives])
    
