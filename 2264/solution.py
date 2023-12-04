class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                if ans == "":
                    ans = num[i]
                else:
                    ans = max(num[i], ans)
        return f'{ans}{ans}{ans}'
