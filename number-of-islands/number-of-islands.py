class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len( grid )
        n = len( grid[0] )
        
        def recursive( i, j ):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
                return
            
            grid[i][j] = '#'
            
            for move_x, move_y in [ (0,1),(1,0),(0,-1),(-1,0)]:
                recursive(i+move_x,j+move_y)
        
        count = 0
        for i in range( m ) :
            for j in range( n ) :
                if grid[i][j] == "1":
                    count += 1
                else:
                    continue
                recursive( i, j )
                
        return count