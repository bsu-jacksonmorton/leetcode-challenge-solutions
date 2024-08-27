class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # create our graph ds
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u,prob))
        dist = [0.0] * n
        dist[start_node] = 1.0
        q = deque([start_node])
        while q:
            curr_node = q.popleft()
            for next_node, prob in graph[curr_node]:
                if dist[curr_node] * prob > dist[next_node]:
                    dist[next_node] = dist[curr_node] * prob
                    q.append(next_node)
        return dist[end_node]
