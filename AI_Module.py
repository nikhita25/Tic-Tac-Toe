def AIMove(board,player):
    #is there any room on the board for anyone to move
    def isMovePossible(board):
        for i in range(len(board)):
            for j in range(len(board)):
                if(board[i][j] == 0):
                    return True
        return False

    def checkWinCondition(board):
        #check diagonals, just hardcode it only 2 diagonals anyway
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            #player 1
            if(board[0][0] == 1):
                return 10
            #player 2 
            if(board[0][0] == 2):
                return -10
        if (board[0][2] == board[1][1] and board[1][1]== board[2][0]):
            #player 1
            if(board[1][1] == 1):
                return 10
            #player 2 
            if(board[1][1] == 2):
                return -10
        #check row/columns
        for i in range(0,3):
            #check each row for matching 3 set
            if (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
                #player 1
                if(board[i][0] == 1):
                    return 10
                #player 2 
                if(board[i][0] == 2):
                    return -10
            #check each column
            if (board[0][i] == board[1][i] and board[1][i] == board[2][i]):
                #player 1
                if(board[0][i] == 1):
                    return 10
                #player 2 
                if(board[0][i] == 2):
                    return -10

            #no winners yet
        return 0
    #bascially checks every permutation possible recursvely until someone wins or ties
    def stockFish(board, turn, player):
        score = checkWinCondition(board)
        #print(board,player,score)
        #player 1 win
        if(score == 10):
            return score
        #player 2 win
        if(score == -10):
            return score
        #is Tie no move possible and no one won
        if(isMovePossible(board) == False):
            return 0
        #checking for player1's best move score
        if(player):
            #is negative since we want a higher score
            best = -1000
            #For every open square make a move
            for i in range(len(board)):
                for j in range(len(board)):
                    if(board[i][j] == 0):
                        board[i][j] = 1
                        #print('test:',board,player,i,j)
                        #calls itself so the opponent can make a move, will return the highest score 
                        best = max(best, stockFish(board, turn+1,not player))
                        board[i][j] = 0
            return best
        else:
            #positive to get lowest score
            best = 1000 
            #same as above but with o's
            for i in range(len(board)):
                for j in range(len(board)):
                    if(board[i][j] == 0):
                        board[i][j] = 2
                        #calls itself so the opponent can make a move, will return the lowest score 
                        best = min(best, stockFish(board, turn+1,not player))
                        board[i][j] = 0
            return best
    #given every possible move what would result in a win or a tie, win perferable
    #will print out [-1,-1] if you input in a full board
    def findBestMove(board,player):
        bestMove = [-1,-1]
        #player 1 starts negative since we want to get that 10 or 0
        if(player == 1):
            bestVal = -1000
        #player 2 starts positive since we want a -10 or 0
        if(player == 2):
            bestVal = 1000
        #for every blank square make a move with either x or o
        for i in range(len(board)):
                for j in range(len(board)):
                    if(board[i][j] == 0):
                        if(player == 1):
                            #makes a possible move
                            board[i][j] = 1
                            #evauates that move, is false since True is player 1 and player 1 just 'moved'
                            moveVal = stockFish(board, 0, False)
                            #print('moveVal:',moveVal)
                            #undoes the move to allow the next possible move
                            board[i][j] = 0
                            if (moveVal > bestVal):
                                bestMove = [i,j]
                                bestVal = moveVal
                        else:
                            #same as the above but does o's instead of x's
                            board[i][j] = 2
                            moveVal = stockFish(board, 0, True)
                            board[i][j] = 0
                            #print('moveVal:',moveVal)
                            if (moveVal < bestVal):
                                bestMove = [i,j]
                                bestVal = moveVal
        #print('Best Value is:',bestVal)
        return bestMove


    bestMove = findBestMove(board,player)
    return bestMove
