import random
from replit import clear
from day7_hangman_words import word_list
from day7_hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#game logic
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #clear is needed to clear the screen after each input from the user
    clear()

    #handling the repetition of the answer
    if guess in display:
        print(f"You've already guessed this letter, please enter another letter\nCurrent Lives: {lives}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You've entered a letter which is not in the word you're guessing. \nYou lose a life point: {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])