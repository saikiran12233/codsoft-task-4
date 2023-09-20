import random


choices =("rock", "paper", "scissors")

computer =random.choice(choices)
player = input("rock, paper or scissors?: ").lower()

if player not in choices:
    print("Error")
    player = input("rock, paper or scissors?: ").lower()
else:
 print("computer: ", computer)
 print("player: ", player)
 
if player == computer:
    player = input("rock, paper or scissors?: ").lower()
    
elif player =="scissors":
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You win!")

    
        
 
    
