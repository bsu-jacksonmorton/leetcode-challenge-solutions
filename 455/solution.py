class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        sp = 0
        gp = 0
        while sp < len(s) and gp < len(g):
            if s[sp] >= g[gp]:
                sp += 1
                gp += 1
                res += 1
            else:
                sp += 1
        return res
