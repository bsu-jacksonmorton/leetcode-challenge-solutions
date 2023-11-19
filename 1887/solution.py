class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 1:
            return res
        nums.sort(reverse=True)
        i = 0
        while nums[0] != nums[-1] and i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                res += i+1
            i += 1
        return res
