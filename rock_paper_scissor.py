import random

def play():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = input("Enter rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice! Try again.")
        return

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}\n")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose! ")

while True:
    play()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
