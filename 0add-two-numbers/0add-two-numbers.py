# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        result = ListNode()
        prev = result
        carry = 0
        
        while p1 or p2 or carry:
            p1val = p1.val if p1 else 0
            p2val = p2.val if p2 else 0
            
            num = p1val + p2val + carry
            carry, val = num // 10, num % 10
            curr = ListNode(val)
            prev.next = curr
            prev = curr
            
            if p1: p1 = p1.next
            if p2: p2 = p2.next
                
        return result.next
                
            