# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
#code 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        if not root:
            return 0
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        return 1 + max(l,r)
        
'''
#code 2

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l= self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        return 1 + max(l,r)
#'#''