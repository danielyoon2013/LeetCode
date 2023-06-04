# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        in_order_arr = []
        
        def recursive( node ):
            if node.left:
                recursive( node.left )
                
            in_order_arr.append( node.val )
            
            if node.right:
                recursive( node.right )
        
        recursive( root )

        return in_order_arr[k-1]
        #time complexity: O(N)
        #space complexity: O(N)
    
        '''Better Solution
        
        stack = []
        
        while True:
            while root:
                stack.append( root )
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
        
        #time complexity: O(H+k) on average where H is height
        #space complexity: O(H+k) on average
        '''
                