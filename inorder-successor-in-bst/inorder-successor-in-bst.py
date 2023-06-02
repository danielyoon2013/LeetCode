# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        rightmost_node = [None]
        
        def recursive( node ):
            if not node:
                return
            
            elif node.val > p.val:
                rightmost_node[0] = node
                recursive( node.left )
                
            else:
                recursive( node.right )
        
        recursive( root )
        return rightmost_node[0]
                