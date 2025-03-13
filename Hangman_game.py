import random
import hangman_stages
import world_file

def play_hangman():  # Function to play the hangman game
    lives = 6
    chosen_word = random.choice(world_file.words)
    display = ["_" for _ in range(len(chosen_word))]    # Displaying the word as underscores
    print(display)
    
    game_over = False   # Game over flag
    
    while not game_over:    # Loop to play the game
        guessed_letter = input("Guess a letter: ").lower()
        
        if guessed_letter in display:   # If the guessed letter is already guessed
            print(f"You've already guessed '{guessed_letter}'")
            continue    # Continue the loop
        
        # Check guessed letter
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = guessed_letter  # Display the guessed letter in the word

        print(display)
        
        # If guessed letter is not in the word
        if guessed_letter not in chosen_word:
            lives -= 1  # Decrease the lives
            print(f"Wrong guess! You lose a life. Lives remaining: {lives}")
            if lives == 0:
                game_over = True
                print("You lose!!")
                print(f"The word was '{chosen_word}'.")

        # Check if user has guessed all letters
        if "_" not in display:  # If all the letters are guessed
            game_over = True
            print("You won!!")  # Display the message
        
        # Display the current hangman stage
        print(hangman_stages.stages[lives])

    return game_over    # Return the game over flag

def main(): # Main function
    game_over = False   # Game over flag
    while True: # Loop to play the game
        game_over = play_hangman()
        play_again = input("Type 'yes' to continue, type 'no' to exit.\n").lower()  # Ask user to play again
        if play_again == 'no':  # If user wants to exit
            print("Have a nice day! Bye..")
            break   # Break the loop

if __name__ == "__main__":  # Run the main function
    main()  # Call the main function