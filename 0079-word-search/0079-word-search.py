class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        # My solution
        '''
        def backtrack(i, j, idx):
            
            if i < 0 or j  < 0 or i >= n or j >= m or board[i][j] != word[idx] or board[i][j] == "#" :
                return False
            
            if board[i][j] == word[idx] and idx == len(word)-1:
                return True
            
            for move in [ (0,1), (1,0), (0,-1), (-1,0) ]:
                temp = board[i][j]
                board[i][j] = "#"
                if backtrack(i+move[0], j+move[1], idx+1):
                    return True
                board[i][j] = temp
                
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True
                
        return False
        '''
        # Cleaner
        def backtrack(i, j, idx):
            
            if i < 0 or j  < 0 or i >= n or j >= m or board[i][j] != word[idx] :
                return False
            
            if board[i][j] == word[idx] and idx == len(word)-1:
                return True
            
            board[i][j] = "#"
            for move_x, move_y in [ (0,1), (1,0), (0,-1), (-1,0) ]:
                if backtrack(i+move_x, j+move_y, idx+1):
                    return True
            board[i][j] = word[idx]
            
            return False
                
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True
                
        return False
        
        # time complexity = O( length of board X 3 ** length of word)
        # space complexity = O( length of word ), because it is dominated by recursion call of backtracking function

