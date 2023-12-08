class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans = 0
        s = []
        seen = set()
        for c in word:
          if c.isalpha():
            if s:
              seen.add("".join(s))
              s = []
          elif c == "0":
            if s and s[0] != "0" or not s:
              s.append("0")
          else:
            if len(s) == 1 and s[0] == "0":
              s.pop()
            s.append(c)
        if s:
          seen.add("".join(s))
        return len(seen)
