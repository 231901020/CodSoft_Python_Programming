import random

def play_game():
    # Possible choices
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        # Get user input
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if user_choice == "exit":
            print("Thanks for playing!")
            print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        # Display current scores
        print(f"Scores -> You: {user_score}, Computer: {computer_score}")

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
