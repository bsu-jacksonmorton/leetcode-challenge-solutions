class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True
        direction = -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                if direction == 0:
                    return False
                if direction == -1:
                    direction = 1
            elif nums[i] > nums[i+1]:
                if direction == 1:
                    return False
                if direction == -1:
                    direction = 0
        return True
