import random

user_choice = input("Select rock, paper, or scissors: ")
computer_choice = random.choice(("rock", "paper", "scissors"))
if user_choice == computer_choice:
    print("The computer chose the same as you.")
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("The computer chose scissors.")
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("The computer chose rock.")
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("The computer chose paper.")
    print("You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("The computer chose paper.")
    print("You lose!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("The computer chose scissors.")
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("The computer chose rock.")
    print("You lose!")
