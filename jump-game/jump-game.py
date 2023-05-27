class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = [0]*len(nums)
        n = len(nums)-1
        
        def recursive( start_idx ):
            
            if start_idx == n:
                return True
            
            steps = nums[start_idx]
            
            if steps == 0:
                return False
            
            for step in range(steps,0,-1):
                if start_idx + step <= n and memo[start_idx+step] >= 0 and recursive( start_idx + step ) :
                    return True
            
            memo[start_idx] = -1
            return False
        
        return recursive( 0 )