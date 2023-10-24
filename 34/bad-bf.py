class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # dumb brute force solution
        res = [-1, -1]
        i = 0
        while i < len(nums) and nums[i] != target:
            i += 1
        if i < len(nums) and nums[i] == target:
            res = [i,i]
        else:
            return res
        while i < len(nums) and nums[i] == target:
            i += 1
        if nums[i - 1] == target:
            res[1] = i - 1
        return res
