
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.__inOrderTraversal(root.left, root.right)
        
    def __inOrderTraversal(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == t2 == None:
            return True
        if (t1 is None and t2 is not None) or (t2 is None and t1 is not None):
            return False
        if t1.val != t2.val:
            return False
        else:
            return self.__inOrderTraversal(t1.left, t2.right) and self.__inOrderTraversal(t2.left, t1.right)