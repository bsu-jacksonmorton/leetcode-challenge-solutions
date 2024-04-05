class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Boyer-moore majority vote algorithm
        Runtime: O(n)
        Space: O(1)
        '''
        c = None
        count = 0
        for num in nums:
            if c == None or count == 0:
                c = num
                count = 1
            elif c == num:
                count += 1
                if count > len(nums) // 2:
                    break
            else:
                count -= 1
        return c
