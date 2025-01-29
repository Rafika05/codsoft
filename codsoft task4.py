import sys
import random

def playgame():
    user_score = 0
    computer_score = 0
    while True:
        print("\nChoose: 1. Rock, 2. Paper, or 3. Scissors")
        try:
            user_choice = int(input("Enter your choice (1, 2, 3): "))
        except ValueError:
            print("Invalid input! Please enter 1, 2, or 3.")
            continue

        if user_choice not in [1, 2, 3]:
            print("Invalid choice. Please try again!")
            continue

        if user_choice == 1:
            user_choice_str = "rock"
        elif user_choice == 2:
            user_choice_str = "paper"
        else:
            user_choice_str = "scissors"
            
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer choose: {computer_choice}")


        if user_choice_str == computer_choice:
            print("It's a tie!")
        elif (user_choice_str == "rock" and computer_choice == "scissors") or  (user_choice_str == "scissors" and computer_choice == "paper") or (user_choice_str == "paper" and computer_choice == "rock"):
            print("You win!!")
            print("Computer lose!!")
            user_score += 1
        else:
            print("Computer win!!")
            print("You lose!!")
            computer_score += 1

        print(f"Scores :\n You: {user_score}\nComputer: {computer_score}")

        
        print("\n\t\t1. Play again\n\t\t2. New game\n\t\t3. Quit")
        choice = input("Enter your choice (1, 2, 3): ")

        if choice == "1":
            continue
        elif choice == "2":
            print(f"Final Scores :\n You: {user_score} \n Computer Score: {computer_score}")
            return playgame()
        elif choice == "3":
            print(f"Final Scores :\n You: {user_score} \n Computer: {computer_score}")
            print("\nThanks for playing!.....")
            sys.exit()
        else:
            print("Invalid choice..... Exiting the game......")
            sys.exit()

playgame()
