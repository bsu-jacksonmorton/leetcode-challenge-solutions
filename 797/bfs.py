class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        q = [[0, [0]]]
        while q:
            curr = q.pop(0)
            # found path so add to ans
            if curr[0] == len(graph) - 1:
                ans.append(curr[1])
            else:
              for num in graph[curr[0]]:
                  q.append([num, curr[1] + [num]])
        return ans
