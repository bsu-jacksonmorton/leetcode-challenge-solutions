# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    level-order traversal using BFS
    runtime: O(n)
    space: O(n)
    '''
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        q = [root]
        level = 0
        while q:
            level += 1
            if level == depth - 1:
                break
            for _ in range(len(q)):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        for node in q:
            save_left = node.left
            save_right = node.right
            node.left = TreeNode(val=val, left=save_left)
            node.right = TreeNode(val=val, right=save_right)
        return root
