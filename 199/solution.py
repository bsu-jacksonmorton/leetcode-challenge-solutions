# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Runtime: O(n)
    Space: O(m) where m is the level with the most nodes
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = []
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
                if node and i == n - 1:
                    ans.append(node.val)
        return ans
        
