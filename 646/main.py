class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda k: k[1])
        res = 1
        prev = None
        for i in range(len(pairs)):
            if prev:
                if prev[1] < pairs[i][0]:
                    res += 1
                    prev = pairs[i]
            else:
                prev = pairs[i]
        return res
                
