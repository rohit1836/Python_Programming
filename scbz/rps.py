




# score = 0


# ans = "y"

# while ans == "y":
# print("===================Welcome to Rock Paper Scissores Game===================")

# print()
# print()

# print("1. Rock")
# print("2. Paper")
# print("3. Scissors")


# choice = int(input(("Enter your choice : ")))







# Number guessing game



import random



playerChoice = input("Choose a number between 1 and 50 : ")

computerChoice = random.randint(1,50)

while playerChoice != computerChoice:

    if playerChoice == computerChoice:
        print("Your guesses correct!")

    else:
        print("You guessed wrong!")
        input("Enter again : ")



























