# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque( [root] )
        result = []
        in_order = True
        
        while q:
            n = len(q)
            temp = []
            for i in range(n):
                node = q.popleft()
                
                if in_order:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            in_order = not in_order
            result.append(temp)
            
        return result
                    
                    
                    
                