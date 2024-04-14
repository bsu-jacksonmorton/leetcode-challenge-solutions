# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        '''
        runtime: O(n)
        space: O(n) // call stack space
        '''
        def dfs(root, isLeft):
            if not root:
                return 0
            if not root.left and not root.right and isLeft:
                return root.val
            else:
                return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)
