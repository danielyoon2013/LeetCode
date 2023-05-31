class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        
        def backtrack( path, not_used ):
            if len(not_used) == 0:
                combinations.append(path[:])
                return
            
            element = not_used.pop()
            backtrack( path + [element], not_used )
            backtrack( path, not_used )
            not_used.append(element)
            
        backtrack([], nums)
        return combinations
    
        '''
        def backtrack( first=0, curr=[]):
            if len(curr)==k:
                output.append(curr[:])
                return
            for i in range( first, n ):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return output
        '''