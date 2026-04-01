# while True:
#     player1=input("CHOOSE :ROCK,PAPER OR SEASOR :").lower()
#     player2=input("CHOOSE :ROCK,PAPER OR SEASOR :").lower()

#     if player1_input == player2_input:
#                 print("Tie!")

#     elif player1_input =="rock":
#             if player2_input == "paper":
#                     print("player 1 wins!")
#             else:
#                     print("player 2 wins!")


#     elif player1_input =="paper":
#             if player2_input == "rock":
#                     print("player 1 wins!")
#             else:
#                     print("player 2 wins!")


#     elif player1_input =="rock":
#             if player2_input == "seasor":
#                     print("player 1 wins!")
#             else:
#                     print("player 2 wins!")


#     elif player1_input =="seasor":
#             if player2_input == "paper":
#                     print("player 1 wins!")
#             else:
#                     print("player 2 wins!")


while True:
    player1 = input("CHOOSE: ROCK, PAPER OR SCISSORS: ").lower()
    player2 = input("CHOOSE: ROCK, PAPER OR SCISSORS: ").lower()

    if player1 == player2:
        print("Tie!")
    
    elif player1 == "rock":
        if player2 == "paper":
            print("Player 2 wins!")
        elif player2 == "scissors":
            print("Player 1 wins!")
    
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")
    
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!")
        elif player2 == "rock":
            print("Player 2 wins!")
    
    else:
        print("Invalid input! Please choose rock, paper, or scissors.")
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        break
    





    
