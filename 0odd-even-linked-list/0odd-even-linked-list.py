# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head, even_head = ListNode(), ListNode()
        odd_prev, even_prev = odd_head, even_head
        even_curr, odd_curr = ListNode(),ListNode()
        
        ptr = head
        i = 0
        
        while ptr:
            
            if i % 2 == 0:
                print( ptr.val )
                even_curr = ptr
                even_prev.next = ptr
                even_prev = ptr
            else:
                odd_curr = ptr
                odd_prev.next = ptr
                odd_prev = ptr
            
            ptr = ptr.next
            i+=1
        
        odd_curr.next = None
        even_curr.next = odd_head.next
        
        return even_head.next