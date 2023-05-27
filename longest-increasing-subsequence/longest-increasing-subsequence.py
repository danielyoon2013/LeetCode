class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # let i : start idx
        # let j : end idx
        # let dp[i] be length of longest substring that ends with nums[i]
        # dp[j] = max( dp[k] ) + 1 where k = nums[k] < nums[j]
        
        # initialize dp
        dp = [1] * len(nums)
        
        for j in range(1,len(nums)):
            for k in range(j):
                if nums[j] > nums[k]:
                    dp[j] = max( dp[k] + 1, dp[j] )
        
        return max(dp)
                    
        