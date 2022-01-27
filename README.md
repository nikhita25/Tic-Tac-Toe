# Tic Tac Toe

### By Rupert, David and Nikhita

## How to use:

 1. The program runs from the menu.py file. Enter **python menu.py** to run the function. 
 2. A pygame window will open with the game menu. Here you can choose to play Single Player, Multi Player or to quit.
 ![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT1.PNG?raw=true)

 3. Click on **Single** to play against the AI. A window will open with 9 boxes, click on one of the boxes to make your move. Since you are playing against the AI, the computer's move will show up automatically. 
 
![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT2.PNG?raw=true)
 


 4. The player will be '**O**' and the computer will play as '**X'**. 
 
 You can either win, lose or tie the game. A line will appear showing the winning moves and a message will appear: 
![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT3.PNG?raw=true)
 5. After the game a menu will appear on the screen, you can choose to retry or go back to the main menu
 ![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT4.PNG?raw=true)
 
 6. If a player wants to play again, they can click retry and it will take the user to a new board:  ![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT11.PNG?raw=true)
 
 7. If they click on menu, they will be taken back to the main menu. To play with someone else, click on **Multi** to play a 2 player game, the board will look similar. 
![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT9.PNG?raw=true)

 8. Similar to single player, click on the screen to make your move. Player 1 will play as '**O**' and Player 2 will play as '**X**'. Once no more moves need to be made, the game will annouce the winner or a tie. Multi player has a score board which keeps track of the scores. 

 ![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT5.PNG?raw=true)
 

 9. The score board is updated after every game, but the score will be lost once the players exit the program. Previously Player 1 won, so they had one point. Here player 2 won, and will be given one point. But if the game is a tie, neither player gets a point. 
 ![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT10.PNG?raw=true)

 10. The players can either replay the game or go back to the main menu. Here if the "Quit" button is clicked, the program will end. 
![alt text](https://github.com/nikhita25/Tic-Tac-Toe/blob/main/Images/TTT12.PNG?raw=true)

## The code
There are comments on the code explaining what each function does. Here is a brief description of what each file contains:

### Menu .py by Rupert,Nikhita
The menu.py file contains the lenght, color and display for the main menu screen. We created 3 buttons and if statements for what happens when each of the buttons are clicked. The main() function loops through the menu and the game code.

### Game .py by Rupert,David
The game.py file contains the length, color and display of the game board. 

 - **drawLines()** - draws the board and the lines for the tic tac toe game
 - **drawShapes()** - draws the 'X' and 'O' when the game is being played
 - **markSquare()** - when a player makes a move, it is added onto the board
 - **availableSquare()** - checks to see if there any avaible spots left on the board
 - **isFullBoard()** - checks to see if all the spots are filled on the board
 - **checkWin()** - looks to see if there is a winner
 - **drawVerticalLine, drawHorizontalLine, drawAscDiagonalLine, drawDescDiagonalLine** - these functions draw the line over the winning three boxes

This file also contains the Multi_Player and Single_Player to code the Multi and single player games respectively.

### Al_Module .py by Rupert
The AI_Module.py file has functions used to code Single_Player().  

 - **isMovePossible()** - checks if there are any more possible moves on the board
 - **checkWinCondition()** - checks diagnoally, horizontally and   
   vertically to see if there is a winner. 
 - **stockFish()** - checks every    permutation possible recursvely until
   someone wins or ties    
 - **findBestMove()** - checks to find the next best move

