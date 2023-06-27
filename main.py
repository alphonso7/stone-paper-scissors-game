import random
print("Let's play Stone paper scissors game")
print("---------------------")
user_turn=input("Enter your choice(stone, paper, scissors): ")
possible_outcome=["stone", "paper", "scissors"]
comp_turn=random.choice(possible_outcome)
print("Computer choose :", comp_turn)
if user_turn == comp_turn:
    print("Its a tie")
elif user_turn == "stone" and comp_turn == "paper":
    print(" You lost")
elif user_turn == "paper" and comp_turn == "stone":
    print(" You won")
elif user_turn == "stone" and comp_turn == "scissors":
    print(" You won")
elif user_turn == "scissors" and comp_turn == "stone":
    print("You lost")
elif user_turn == "paper" and comp_turn == "scissors":
    print("You lost")
elif user_turn == "scissors" and comp_turn == "paper":
    print("You won")
 
    
