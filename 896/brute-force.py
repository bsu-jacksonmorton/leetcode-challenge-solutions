class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True
        decrease = True
        # check increasing
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                increase = False
                break
        # check decreasing
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                decrease = False
                break
        return increase or decrease
