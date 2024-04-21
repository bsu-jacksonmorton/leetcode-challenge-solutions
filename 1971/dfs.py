class Solution:
    '''
    DFS
    runtime: O(v + e)
    space: O(v)
    '''
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        seen = set([source])
        graph = defaultdict(list)
        for edge in edges:
            x, y = edge
            graph[x].append(y)
            graph[y].append(x)
        def dfs(curr):
            if curr == destination:
                return True
            seen.add(curr)
            for node in graph[curr]:
                if node not in seen:
                    if dfs(node):
                        return True
            return False
        return dfs(source)
