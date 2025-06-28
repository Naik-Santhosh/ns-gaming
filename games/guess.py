import time, random, os

os.system('clear') #clearing the terminal

def guessing():
    print("Welcome to Guessing Game")
    instList = ["You will start at Level 1 and level up as you win.",
                    "In each level, you must guess a random number within a certain range.",
                    "The number of attempts will decrease as levels increase.",
                    "You win a level by guessing the correct number within the allowed attempts.",
                    "You lose the game if you run out of attempts in any level.",
                    "You can type 'exit' anytime to quit the game.",
                    ]
    for i, instlist in enumerate(instList, start = 1):
            time.sleep(0.05)
            print(f"{i}.{instlist}")
    print()

    print("----Here you get total 10 levels ")
    levelList = ["Level 1 = range: 1-30, max attempts: 7",
                    "Level 2 = range: 1-50, max attempts: 6",
                    "Level 3 = range: 1-100, max attempts: 5",
                    "Level 4 = range: 1-150, max attempts: 5",
                    "Level 5 = range: 1-200, max attempts: 4",
                    "Level 6 = range: 1-300, max attempts: 4",
                    "Level 7 = range: 1-500, max attempts: 3",
                    "Level 8 = range: 1-750, max attempts: 3",
                    "Level 9 = range: 1-1000, max attempts: 2",
                    "Level 10 = range: 1-1500, max attempts: 2"
                    ]
    for i, levellist in enumerate(levelList, start = 1):
            time.sleep(0.05)
            print(f"{i}.{levellist}")
        
        
    print()
    start_time = time.time()
    player_name = input("Enter your name: ")

    file_path = "games/score.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()

            player_data = {}

            for line in lines:
                key, value = [x.strip() for x in line.strip().split("=")]
                if key == "name":
                    player_data[key] = value
                else:
                    player_data[key] = int(value)
        
        print(f"Welcone back {player_data['name']}! you are at level {player_data['level']}, you won the matches are {player_data['wins']} and losses are {player_data['losses']}.")

    else:
        player_data = {
            "name" : player_name,
            "level" : 1,
            "wins" : 0,
            "losses" : 0,
        }

        print(f"welcome {player_data['name']}! Starting a new game from level 1")
                    


    level = player_data["level"]
    while True:
        level = player_data["level"]
        if level == 1:
            maxRan = 30
            attempt = 7
        elif level == 2:
            maxRan = 50
            attempt = 6
        elif level == 3:
            maxRan = 100
            attempt = 5
        elif level == 4:
            maxRan = 150
            attempt = 5
        elif level == 5:
            maxRan = 200
            attempt = 4
        elif level == 6:
            maxRan = 300
            attempt = 4
        elif level == 7:
            maxRan = 500
            attempt = 3
        elif level == 8:
            maxRan = 750
            attempt = 3
        elif level == 9:
            maxRan = 1000
            attempt = 2
        elif level == 10:
            maxRan = 1500
            attempt = 2
        else:
            print("Wow! you defeat the hardcore level")
            end_time = time.time()
            time_taken = round(end_time - start_time)
            with open(file_path,"w") as file:
                for key, value in player_data.items():
                    file.write(f"{key} = {value}\n")

            print(f"Summary of {player_data['name']}! you are at level {player_data['level']}, you won the matches are {player_data['wins']}, losses are {player_data['losses']} and time taken to complete {time_taken}.")

            break

        appreciation_phrases = [
    "Wow, you did it!",
    "Great job!",
    "Awesome work!",
    "Well done!",
    "You nailed it!",
    "Impressive!",
    "Nice coding!",
    "That’s spot on!",
    "Perfect solution!",
    "Flawless execution!"
]



        random1 = random.randint(1,maxRan)

        while attempt > 0:
            guess = input("Enter the quessing number: ").lower().strip()

            if "exit" == guess:
                print("Exiting the match")
                with open(file_path,"w") as file:
                    for key, value in player_data.items():
                        file.write(f"{key} = {value}\n")
                end_time = time.time()
                time_taken = round(end_time - start_time)
                print(f"Summary of {player_data['name']}! you are at level {player_data['level']}, you won the matches are {player_data['wins']}, losses are {player_data['losses']} and time taken to complete {time_taken}.")

                break

            if not guess.isdigit():
                print(f"Enter the number from 1 to {maxRan} or to quit enter 'eixt'.")
                continue
            
            if random1 == int(guess):
                print("Wow! you guessed the corrected answer")
                break
            elif random1 < int(guess):
                print("Too high")
            elif random1 > int(guess):
                print("Too low")
            elif abs(int(guess) - random1) <= 3:
                print("Uff very close")
            attempt -= 1

            print(f"your attempt left are {attempt}")

        if attempt > 0:
            print(f"You won the match")
            print(random.choice(appreciation_phrases))
            print(f"The guessing number is {random1}")
            player_data["level"] += 1
            player_data["wins"] += 1
            print(f"you now jumb to level {player_data['level']} ")
            print(f"in level {level} number range is 0 to {maxRan} and attempt are {attempt}")
            
            continue

        elif attempt == 0:
            print(f"You loose the match")
            print(f"The guessing number is {random1}")
            player_data["losses"] += 1
            end_time = time.time()
            time_taken = round(end_time - start_time)

            with open(file_path,"w") as file:
                for key, value in player_data.items():
                    file.write(f"{key} = {value}\n")
            print(f"Summary of {player_data['name']}! you are at level {player_data['level']}, you won the matches are {player_data['wins']}, losses are {player_data['losses']} and time taken to complete {time_taken}.")

            
                
            print("You want play one more time or you want to exit")
            choice = input("Enter 'yes' for play game or 'no' for exit the game: ")
            if choice == "no":
                print("Exitting the guessing game: ")

                end_time = time.time()
                time_taken = round(end_time - start_time)

                with open(file_path,"w") as file:
                    for key, value in player_data.items():
                        file.write(f"{key} = {value}\n")
                break
                    
            elif choice == "yes":
                print("replaying the game")
                print()
                level = 1
        


guessing()