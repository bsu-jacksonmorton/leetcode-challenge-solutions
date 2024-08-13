class Solution:
    '''
    O(2^n) - runtime
    O(n) - space
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or curr_sum > target:
                return
            # include i
            curr.append(candidates[i])
            backtrack(i+1, curr, curr_sum + candidates[i])
            # dont include i
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr, curr_sum)
        backtrack(0, [], 0)
        return res
