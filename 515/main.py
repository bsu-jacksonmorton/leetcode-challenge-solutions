 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        while q:
            curr_max = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    curr_max = max(curr_max, node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curr_max != float("-inf"):
                res.append(curr_max)
        return res
