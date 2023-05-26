class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        A = abs( ( ax1 - ax2 ) * ( ay1 - ay2 ) )
        print( "A:" + str( A ) )
        B = abs( ( bx1 - bx2 ) * ( by1 - by2 ) )
        print( "B:" + str( B ) )
        
        IsOverlap = \
        ( min( ay1, ay2 ) <= max( by1, by2 ) <= max( ay1, ay2 )
        or min( by1, by2 ) <= max( ay1, ay2 ) <= max( by1, by2 ) ) \
        and \
        ( min( ax1, ax2 ) <= max( bx1, bx2 ) <= max( ax1, ax2 )
        or min( bx1, bx2 ) <= max( ax1, ax2 ) <= max( bx1, bx2 ) )
        
        OverlapArea = 0
        if IsOverlap:
            arr_X = [ ax1, ax2, bx1, bx2 ]
            arr_Y = [ ay1, ay2, by1, by2 ]
            
            arr_X.sort()
            arr_Y.sort()
            
            OverlapArea = abs( ( arr_X[1] - arr_X[2] ) * ( arr_Y[1] - arr_Y[2] ) )
         
        
        print( "OverlapArea:" + str( OverlapArea ) )
        return A + B - OverlapArea
            
            
        
        
        