class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x = 0 
        o = 0 
        x_wins = False
        o_wins = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    x+=1
                elif board[i][j] == "O":
                    o+=1
            if board[i] == "XXX":
                x_wins = True
            elif board[i] == "OOO":
                o_wins = True
            column = board[0][i] + board[1][i]  + board[2][i]
            if column == "XXX":
                x_wins = True
            elif column == "OOO":
                o_wins = True
        diagonal_1 = board[0][0] + board[1][1] + board[2][2]
        diagonal_2 = board[0][2] + board[1][1] + board[2][0]
        if diagonal_1 == "XXX" or diagonal_2 == "XXX":
            x_wins = True
        if diagonal_1 == "OOO" or diagonal_2 == "OOO":
            o_wins = True

        if x_wins and o_wins:
            return False
        
        if x_wins:
            return x - o == 1
        elif o_wins:
            return x == o
        else:
            return x >= o and x - o <= 1
        

            
            