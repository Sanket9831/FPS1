# Print the Game Instruction to the User/Player 
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs paper   -> paper wins \n"
                                +"\tRock  vs scissor -> Rock wins \n"
                                +"\tpaper vs scissor -> scissor wins \n") 

while True:


    
    # Get the response from User to Play Again    
    ans = input("Do you want to play again ? (Y/N) > ") 
  
    # Check the response from User and continue the loop
    # Othewise break the loop to close the game
    if (ans == 'n' or ans == 'N') : 
        break
    
    
# Print a Thanks Message to the user
print("\nThanks for playing Rock Paper Scissor Game \n") 