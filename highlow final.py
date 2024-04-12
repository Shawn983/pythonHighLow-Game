# HighLow Game
#Importing random module
import random
#Start the game
def play_game():
    coins = 0
    while True:
        # Generate two random numbers(1st will not be revealed, 2nd will be revealed)
        random_number_1 = random.randint(0, 100)
        random_number_2 = random.randint(0, 100)

        # user guess
        guess = input(f"Is the secret number higher, lower, or the same as {random_number_2}? ").lower()
        print(f"The secret number was: {random_number_1}")

        # Check if guess is correct and add 100 coins if it is correct
        if (guess == "higher" and random_number_1 > random_number_2) or  (guess == "lower" and random_number_1 < random_number_2) or (guess == "same" and random_number_1 == random_number_2):
            print("You Win!")
            coins += 100
            print(f"You've earned 100 coins. Total coins: {coins}")
        else:
            print("You Lose!")

        # Check for Champion Status
        if coins >= 500:
            print("Congratulations! You are the champion!")
            break

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()
