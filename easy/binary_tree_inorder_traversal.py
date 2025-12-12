"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
                
s = Solution()


'''
t5 = TreeNode(6)
t4 = TreeNode(5)
t3 = TreeNode(4)
t2 = TreeNode(3,t5)
t1 = TreeNode(2,t3,t4)
t0 = TreeNode(1,t1,t2)
'''
#t0 = TreeNode(1)

t8 = TreeNode(9)
t7 = TreeNode(8,t8)
t6 = TreeNode(7)
t5 = TreeNode(6)
t4 = TreeNode(5,t5,t6)
t3 = TreeNode(4)
t2 = TreeNode(3,None,t7)
t1 = TreeNode(2,t3,t4)
t0 = TreeNode(1,t1,t2)

#te = None
tone = TreeNode(1)
print(s.inorderTraversal(t0))
    