import time, os

from games.guess import guessing
from games.rps import rpsGame

os.system('clear') #clearing the terminal


welcome = "Welcome to Naik's GamesZone"

for i in welcome:
    time.sleep(0.05)
    print(i, end="",flush = True)
print()


gameList = ["Guessing Game.", "Rock Paper scissor.", "Typing Speed Test.", "Word Scrambler.","Quiz Game.", "Exit."]

for i, gamelist in enumerate(gameList, start = 1):
    time.sleep(0.05)
    print(f"{i}.{gamelist}")

while True:
    try:
        choice = int(input("Enter the number to play game: "))
    except ValueError:
        print("Please enter only number")

    if choice == 1:
        guessing()
    elif choice == 2:
        rpsGame()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        print("Exiting the game")
        break
    else:
        print("Enter the number from 1 to 6")



