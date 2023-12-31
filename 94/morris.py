# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr, pre = root, None
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                tmp = curr
                curr = curr.left
                tmp.left = None
        return ans   
