class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        
        def backtrack(path, idx, size_left_paren, size_right_paren):
            
            if idx >= n and (size_left_paren > n or size_right_paren > n ):
                return
            
            if idx == n*2:
                combinations.append(path)
            
            if size_left_paren >= size_right_paren:
                backtrack(path+"(", idx+1, size_left_paren+1, size_right_paren)
                backtrack(path+")", idx+1, size_left_paren, size_right_paren+1)
        
        backtrack("",0,0,0)
        return combinations
            
                