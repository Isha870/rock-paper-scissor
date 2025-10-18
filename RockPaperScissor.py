import random

# Options for the game
options = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Optional: Initialize scores
user_score = 0
computer_score = 0

# Main game loop
while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower().strip()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        break
    
    if user_choice not in options:
        print("Invalid choice. Try again.")
        continue
    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    print("-" * 20)
    
    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

