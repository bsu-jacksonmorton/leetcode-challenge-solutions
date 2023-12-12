class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # single pass approach O(n)
        i, j = 0, 0
        for num in nums:
            if num > i:
                j = i
                i = num
            else:
                j = max(j,num)
        return (i-1) * (j-1)
