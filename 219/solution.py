class Solution:
    '''
    Runtime: O(n)
    Space: O(n)
    '''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in m:
                if abs(i - m[val]) <= k:
                    return True
                else:
                    m[val] = i
            else:
                m[val] = i
        return False
