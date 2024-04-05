# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    runtime: O(n)
    space: O(n)
    '''
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        queue = [root]
        ans = []
        while queue:
            curr = queue.pop(0)
            if curr.left:
                parents[curr.left.val] = curr
                queue.append(curr.left)
            if curr.right:
                parents[curr.right.val] = curr
                queue.append(curr.right)
        visited = {}
        queue.append(target)
        # now we do a level order kind of traversal for k levels
        while k and queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                visited[curr.val] = 1
                if curr.left and curr.left.val not in visited:
                    queue.append(curr.left)
                if curr.right and curr.right.val not in visited:
                    queue.append(curr.right)
                if curr.val in parents and parents[curr.val].val not in visited:
                    queue.append(parents[curr.val])
            k -= 1
        for node in queue:
            ans.append(node.val)
        return ans
        
