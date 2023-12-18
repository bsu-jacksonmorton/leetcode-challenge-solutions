class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        big1, small1 = 0, inf
        big2, small2 = 0, inf
        for num in nums:
            if big1 < num:
                big2 = big1
                big1 = num
            elif big2 < num:
                big2 = num
            if small1 > num:
                small2 = small1
                small1 = num
            elif small2 > num:
                small2 = num
        return (big1 * big2) - (small1 * small2)
