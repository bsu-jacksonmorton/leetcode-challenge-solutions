"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Runtime - O(n)
# Space - O(n) - call stack
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            if not node.children or len(node.children) == 0:
                ans.append(node.val)
                return
            for child in node.children:
                dfs(child)
            ans.append(node.val)
        dfs(root)
        return ans
