class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        most = -1
        for num in candies:
            most = max(most, num)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= most:
                res[i] = True
        return res
