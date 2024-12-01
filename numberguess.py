import random

#Random number generator between 1 and 100
def generate_number():
    return random.randint(1,100)

#Provide the user a clue based on their guess
def clue(number,guess):
    if guess > number:
        return "The number is greater than your guess."
    elif guess < number:
        return "The number is smaller than your guess."
    else:
        return "You've guessed the number!"
#Main game
def play_game():
    number = generate_number()
    score = 100
    attempts = 0

    while True:
        #Prompts user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        #Checks if the guess is correct
        if guess == number :
            print(f"Congratulations! You got the correct guess in {attempts} attempts")
            break
        else:
            clues = clue(number,guess) # Get a clue based on the guess
            score -= 10
            print(clues)
            print(f"Score: {score}")

if __name__ == "__main__":
    play_game()

