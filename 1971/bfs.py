class Solution:
    '''
    BFS
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
        q = [point for point in graph[source]]
        while q:
            curr = q.pop(0)
            if curr == destination:
                return True
            for point in graph[curr]:
                if point not in seen:
                    seen.add(point)
                    q.append(point)
        return False
