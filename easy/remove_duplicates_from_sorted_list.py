"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        prev = None
        while head != None:
            if prev != None and head.val == prev.val:
                prev.next = head.next
                head = prev
            if head.next != None and head.val == head.next.val:
                head.next = head.next.next
                prev = head
            head = head.next
                
        return start
    
    
s = Solution()
    
l0 = ListNode(1)
l1 = ListNode(1,l0)
l2 = ListNode(1,l1)
    
x = s.deleteDuplicates(l2)

while x != None:
    print(x.val)
    x = x.next