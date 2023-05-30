class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        
        def backtracking( not_used, path ):
            if len(not_used) == 0:
                combinations.append(path[:])
                return
            
            for i in range(len(not_used)):
                element = not_used.pop(0)
                backtracking( not_used.copy(), path+[element])
                not_used.append(element)
            
        backtracking(nums,[])
        return combinations
        