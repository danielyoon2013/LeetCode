class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        
        def backtrack( path, not_used ):
            if len(not_used) == 0:
                combinations.append(path)
                return
            
            element = not_used.pop()
            backtrack( path + [element], not_used )
            backtrack( path, not_used )
            not_used.append(element)
            
        backtrack([], nums)
        return combinations
