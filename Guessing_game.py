import random
logo = """ 
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      """
print(logo)
# choosing a random number from 1:100
guess_number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# choosing a level of game
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# depending of game level nuber of lives
if level == "hard":
    lives = 5
elif level == "easy":
    lives = 10
    print("You have 10 attempts remaining to guess the number.")
# main loop of game
def game(lives):
    guess = 101
    while guess != guess_number and lives != 0:
        # player guessing number
        guess = int(input("Make a guess: "))
        # checking conditions and executing
        if guess < guess_number:
            print("Too low")
            lives -= 1
            print("Guess again.")
            print(f"You have {lives} attempts remaining to guess the number.")
        elif guess > guess_number:
            print("Too high")
            print("Guess again.")
            print(f"You have {lives} attempts remaining to guess the number.")
            lives -= 1
    # finish game with positive result
    if guess == guess_number:
        print(f"You got it! The answer is {guess_number}")
    # finish game with negative result
    elif lives == 0:
        print("You've run out of guesses, you lose.")
game(lives)





