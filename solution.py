# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    runtime: O(n^2)
    space: O(n^2)
    '''
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        def dfs(node, word):
            nonlocal ans
            # reached the end of the tree so lets do our computations on this result
            if not node:
                return
            c = chr(node.val + 97)
            word = c + word
            # check if leaf node
            if not node.left and not node.right:
                if not ans or ans > word:
                    ans = word
            # not a leaf node
            else:
                if node.left:
                    dfs(node.left, word)
                if node.right:
                    dfs(node.right, word)
        dfs(root, "")
        return ans
                    
