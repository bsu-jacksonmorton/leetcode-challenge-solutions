class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[nums[0]]]
        rowPtr = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                rowPtr += 1
            else:
                rowPtr = 0
            if rowPtr >= len(res):
                res.append([])
            res[rowPtr].append(nums[i])
        return res
