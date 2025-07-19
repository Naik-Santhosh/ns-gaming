import time, os, random

os.system('clear') #clearing the terminal

def brainAI(level, player, beats, games):
     chance = random.randint(0,100)
     if level == 1:
          return random.choice(games)
     elif level == 2:
          if chance <= 30:
               return beats[player]
          else:
               return random.choice(games)
     elif level == 3:
          if chance <= 90:
               return beats[player]
          else:
               return random.choice(games)
          

def leaderboard():
     try:
          with open("games/scoreRPS.txt", "r") as file:
               data = file.readlines()
     except FileNotFoundError:
          print("Data is not getting...")
          return
     
     leaderboard = []
     for line in data:
          part = line.strip().split(",")
          if len(part) != 4:
               continue
          name, wins, losses, draws = part
          leaderboard.append((name, int(wins), int(losses), int(draws)))

     leaderboard.sort(key = lambda x:x[1], reverse=True)

     for player in leaderboard[:5]:
          print(f"Name:{player[0]}\tWins:{player[1]}\tLossos:{player[2]}\tDraws:{player[3]}")



     

def udate_score(player_name, wins, lost, draw):
     try:
          with open("games/scoreRPS.txt", "r") as file:
               player_data = {}
               for line in file:
                    if not line.strip():
                         continue
                    name,w,l,d = line.strip().split(",")
                    player_data[name] =[int(w),int(l),int(d)]
     except FileNotFoundError:
          print("Uff something went wrong, call to Naik to fix the problem")
     if player_name in player_data:
          player_data[player_name][0] += int(wins)
          player_data[player_name][1] += int(lost)
          player_data[player_name][2] += int(draw)
     else:
          player_data[player_name] = [wins,lost,draw]

     with open("games/scoreRPS.txt", "w") as file:
          for name, score in player_data.items():
               file.write(f"{name.strip()},{score[0]},{score[1]},{score[2]}\n ")
                    

def rpsGame():
    print("Welcome to RPS Game")
    instList =  [
    "Type 'rock', 'paper', or 'scissors' to play.",
    "Type 'exit' to quit the game.",
    "Rock beats Scissors, Scissors beats Paper, Paper beats Rock."]

    for i, instlist in enumerate(instList, start = 1):
            time.sleep(0.05)
            print(f"{i}.{instlist}")
    print()
    games = ['rock','paper','scissor']
    beats = {
         "rock": "paper",
         "paper": "scissor",
         "scissor": "rock"}
    wins = 0
    lost = 0
    draw = 0


    player_name = input("Enter the player name: ").strip()

    try:
         level = int(input("Choose your level: 1,2,3 "))
         
    except ValueError:
         print("Enter the number only")

    while True:
        try:
             
             player = input("Enter 'Rock'|'Paper'|'Sciccor': ").lower().strip()
             cmp = brainAI(level, player, beats, games)
            
             if player == "exit":
                  break
             
             if player not in games:
                  print("please enter valid name") 
                  continue 
                    
             if player == "rock" and cmp == "paper" or player == "scissor" and cmp == "rock" or player == "paper" and cmp == "scissor":
                  print(f"Player chosen {player} and Computer chosen {cmp}")
                  print("winner is computer")
                  lost += 1

             elif player == "paper" and cmp == "rock" or player == "rock" and cmp == "scissor" or player == "scissor" and cmp == "paper":
                  print(f"Player chosen {player} and Computer chosen {cmp}")
                  print("Player is the winner")
                  wins += 1

             elif player == cmp:
                  print(f"Player chosen {player} and Computer chosen {cmp}")
                  print("It is a draw")
                  draw += 1

             
             
        except ValueError:
             print("Please enter valid name")
          
    print(f"You won {wins} times, lost {lost} times and draw are {draw} time")   

    udate_score(player_name, wins, lost, draw)
    leaderboard()
    
   


