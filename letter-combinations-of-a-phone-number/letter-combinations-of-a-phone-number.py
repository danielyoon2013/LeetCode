class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        
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
            
                
        return recursive( [], 0 )
            