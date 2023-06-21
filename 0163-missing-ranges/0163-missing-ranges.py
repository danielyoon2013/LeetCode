class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        '''my solution
        
        result = []
        
        lowest, uppest = lower-1, upper+1
        
        new_nums = [lowest]
        for num in nums:
            if num < lowest:
                continue
            if num > uppest:
                break
            new_nums.append(num)
        new_nums.append(uppest)
        
        for i in range(len(new_nums)-1):
            prev, curr = new_nums[i], new_nums[i+1]
            if curr - prev > 1:
                result.append([prev+1,curr-1])
        
        return result
        '''
        
        n = len(nums)
        result = []
        
        if n == 0:
            result.append([lower,upper])
            return result
        
        if lower < nums[0]:
            result.append([lower,nums[0]-1])
            
        for i in range(n-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            result.append([nums[i]+1,nums[i+1]-1])
            
        if upper > nums[n-1]:
            result.append([nums[n-1]+1,upper])
            
        return result