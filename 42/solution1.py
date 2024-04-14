class Solution:
    '''
    prefix + postfix approach
    runtime: O(n)
    space: O(n)
    '''
    def trap(self, height: List[int]) -> int:
        ans = 0
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        curr_max = float("-inf")
        for i in range(len(height)):
            curr_max = max(height[i], curr_max)
            max_l[i] = curr_max
        curr_max = float("-inf")
        for i in range(len(height)-1 , -1, -1):
            curr_max = max(height[i], curr_max)
            max_r[i] = curr_max
        for i in range(len(height)):
            ans += min(max_l[i], max_r[i]) - height[i]
        return ans
            
