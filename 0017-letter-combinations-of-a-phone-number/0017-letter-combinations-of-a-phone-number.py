class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        #My Solution
        '''
        def recursive( arr, idx ):
            curr_result = []
            
            if idx == len(digits):
                return arr
            
            digit = digits[idx]
            if digit not in letters.keys():
                return curr_result
            
            for letter in letters[digit]:    
                temp = arr.copy()
                if len( temp ):
                    temp = [ element + letter for element in temp ]
                else:
                    temp = [ letter ]
                curr_result += recursive( temp, idx+1 )
            
            return curr_result
        '''
        
        #Suggested2 BFS
        '''
        if digits == "":
            return []
        
        q = deque(letters[digits[0]])
        
        for i in range( 1, len(digits) ):
            s = len(q)
            
            while s:
                out = q.popleft()
                for j in letters[digits[i]]:
                    q.append( out + j )
                s-=1
        
        return q
         '''       
        
        #Suggested2 DFS
        if len(digits) == 0: 
            return []
        
        combinations = []
        
        def backtrack( index, path ):
            if index == len(digits):
                combinations.append("".join(path))
                return
        
            for letter in letters[digits[index]]:
                path.append(letter)
                backtrack(index+1,path)
                path.pop()
                        
        backtrack(0,[])
        return combinations    