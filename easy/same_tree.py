"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.__inOrderTraversal(p,q)
        
        
    def __inOrderTraversal(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == t2 == None:
            return True
        if (t1 is not None and t2 is None) or (t2 is not None and t1 is None):
            return False
        elif t1.val != t2.val:
            return False
        else:
            return self.__inOrderTraversal(t1.left, t2.left) and self.__inOrderTraversal(t1.right, t2.right)
        
t8 = TreeNode(9)
t7 = TreeNode(8,t8)
t6 = TreeNode(7)
t5 = TreeNode(6)
t4 = TreeNode(5,t5,t6)
t3 = TreeNode(4)
t2 = TreeNode(3,None,t7)
t1 = TreeNode(2,t3,t4)
t0 = TreeNode(1,t1,t2)


t18 = TreeNode(9)
t17 = TreeNode(8,t18)
t16 = TreeNode(7)
t15 = TreeNode(6)
t14 = TreeNode(5,t15,t16)
t13 = TreeNode(4)
t12 = TreeNode(3,None,t17)
t11 = TreeNode(2,t13,t14)
t10 = TreeNode(1,t11,t12)

s = Solution()


print(s.isSameTree(t0,t10))