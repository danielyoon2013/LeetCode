import numpy as np

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def recursive( result, depth ):
            if depth <= len(nums)-1 :

                num = nums[depth]
                new_result = copy.deepcopy(result)
                for e in new_result:
                    e.append(num)

                result = result + new_result
                return recursive( result, depth+1 )

            else:
                return result


        return recursive( [[]], 0 )


            