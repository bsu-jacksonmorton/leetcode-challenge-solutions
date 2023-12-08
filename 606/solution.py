# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
      self.ans = ""
    def preorder(self, node):
      self.ans += str(node.val)
      if node.left or node.right:
        self.ans += "("
      # check left
      if node.left:
        self.preorder(node.left)
      if node.left or node.right:
        self.ans += ")"
      # check right
      if node.right:
        self.ans += "("
        self.preorder(node.right)
        self.ans += ")"
    def tree2str(self, root: Optional[TreeNode]) -> str:
      self.preorder(root)
      return self.ans            
