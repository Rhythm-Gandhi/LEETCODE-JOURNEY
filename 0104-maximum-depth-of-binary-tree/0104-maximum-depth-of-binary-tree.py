# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, root, currDepth):
        if not root:
            return currDepth
        
        left = self.dfs(root.left, currDepth + 1)
        right = self.dfs(root.right, currDepth + 1)

        return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
'''
class Solution:
    def dfs(self,root,depth):
        if not root:
            return depth
        l = self.dfs(root.left,depth+1)
        r = self.dfs(root.right,depth+1)
        return max(l,r)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)
    
        if not root:
            return 0
        return 1 +  max(self.maxDepth(root.left),self.maxDepth(root.right))
        '''

