import random

def playGame():
    userScore = 0
    compScore = 0

    while(compScore < 3 and userScore < 3):
        userChoice = input("Choose rock, paper, or scissors. ")
        print("You chose", userChoice)

        moves = ["rock", "paper", "scissors"]
        compChoice = random.choice(moves)

        if(compChoice == userChoice):
            print("Computer chose", compChoice, ". It's a tie!")
        elif(compChoice == "rock" and userChoice == "scissors"):
            print("Computer chose", compChoice, ". You lose!")
            compScore = compScore + 1
        elif(compChoice == "scissors" and userChoice == "paper"):
            print("Computer chose", compChoice, ". You lose!")
            compScore = compScore + 1
        elif(compChoice == "paper" and userChoice == "rock"):
            print("Computer chose", compChoice, ". You lose!")
            compScore = compScore + 1
        else:
            print("Computer chose", compChoice, "You won!")
            userScore = userScore + 1
        print("Your score:", userScore, ". Computer score:", compScore)
    if(userScore == 3):
        print("You won!")
    else:
        print("You lost!")

playGame()