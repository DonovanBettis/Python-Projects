import random

computer_score = 0
user_score = 0


def getUserChoice():
    print("Please make a selection:")
    choice = input("1. Rock\n2. Paper\n3. Scissors\n").upper()
    if choice == "1":
        return "R"
    if choice == "2":
        return "P"
    if choice == "3":
        return "S"


def getComputerChoice():
    options = "Rock", "Paper", "Scissors"
    computers_choice = random.choice(options)
    if computers_choice == "Rock":
        return "R"
    if computers_choice == "Paper":
        return "P"
    if computers_choice == "Scissors":
        return "S"



def determineWinner(user_choice, computer_choice):
    if user_choice == "R" and computer_choice == "S":
        print("rock smashes scissors")
        return "U"
    if user_choice == "S" and computer_choice == "P":
        print("scissors cuts paper")
        return "U"
    if user_choice == "P" and computer_choice == "R":
        print("paper wraps rock")
        return "U"
    if computer_choice == "R" and user_choice == "S":
        print("rock smashes scissors")
        return "C"
    if computer_choice == "S" and user_choice == "P":
        print("scissors cuts paper")
        return "C"
    if computer_choice == "P" and user_choice == "R":
        print("paper wraps rock")
        return "C"


for i in range(0, 10):

    computer_choice = getComputerChoice()

    user_choice = getUserChoice()
    print(user_choice)
    print("The computer has chosen " + computer_choice)

    while user_choice == computer_choice:
        user_choice = getUserChoice()
        computer_choice = getComputerChoice()

        print("The computer has chosen " + computer_choice)

    winner = determineWinner(user_choice, computer_choice)
    if winner == "C":
        print("The computer wins!")
        computer_score += 1
    if winner == "U":
        print("You win!")
        user_score += 1
    print("\nThe score is:\nComputer: " + str(computer_score) + "\nUser: " + str(user_score) + "\n\n")

if computer_score > user_score:
    print("The computer wins!")
else:
    print("You win!")
