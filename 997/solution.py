class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        m = dict()
        # index 0 is the number of people that trust me
        # index 1 is the number of people that I trust
        for pair in trust:
            a, b = pair
            if a not in m:
                m[a] = [0,0]
            if b not in m:
                m[b] = [0,0]
            m[a][1] += 1
            m[b][0] += 1
        for key in m.keys():
            if m[key][0] == n - 1 and m[key][1] == 0:
                return key
        return -1
