class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n = len(triangle)
        min_path = [ [float('inf')]*(i+1) for i in range(n) ]
        
        min_path[0][0] = triangle[0][0]
        
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    min_path[i][j] = triangle[i][j]  + min_path[i-1][j]
                elif j == len( triangle[i] ) - 1:
                    min_path[i][j] = triangle[i][j]  + min_path[i-1][j-1]
                else:
                    min_path[i][j] = triangle[i][j] + min(min_path[i-1][j-1], min_path[i-1][j])
                    
        return min(min_path[i])
            
            
                
                