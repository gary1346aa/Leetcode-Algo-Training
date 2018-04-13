class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def validation(char):
            char = char + char + char
        
            for row in board:
                if row == char:
                    return True

            if  char == board[0][0] + board[1][0] + board[2][0]:
                return True
            if  char == board[0][1] + board[1][1] + board[2][1]:
                return True
            if  char == board[0][2] + board[1][2] + board[2][2]:
                return True
            if  char == board[0][0] + board[1][1] + board[2][2]:
                return True
            if  char == board[0][2] + board[1][1] + board[2][0]:
                return True
        
            return False
        
        O = 0
        X = 0
        for row in board :
            O += row.count('O')
            X += row.count('X')
            
        if X == O:
            if validation('X') == True:
                return False
            else:
                return True
            
        elif X - O == 1:
            if validation('O') == True:
                return False
            else:
                return True
        else:
            return False