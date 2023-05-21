import numpy as np
from collections import Counter

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        cnt = Counter(word)
            
        if cnt[word[0]] > cnt[word[-1]]:                             
             word = word[::-1]
        
        m, n = len( board ), len( board[0] )
        
        def recursive(i,j,depth):
            
            if depth == len(word):
                return True 
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[depth]:
                board[i][j] = '#'
                moves = [ (i+1,j), (i-1,j), (i,j+1), (i,j-1) ]
                found = any( recursive(ii,jj,depth+1) for ii,jj in moves)
                board[i][j] = word[depth]
                return found
                
            return False
        
        # Loop through all elements in the box as starting point
        for i in range(m):
            for j in range(n):
                if recursive(i,j,0) :
                    return True
    
        return False


    
    
        