class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def binary_search(start, val):
            res = -1
            end = len(stones) - 1
            while start <= end:
                mid = (end+start) // 2
                if stones[mid] == val:
                    res = mid
                    break
                elif stones[mid] < val:
                    start = mid + 1
                else:
                    end = mid - 1
            return res
        
        @cache
        def frog_jump(k, i):
            if i == len(stones) - 1:
                return True
            if i < 0:
                return False
            # going backwards or sitting idle will not work frog man!
            if k <= 0:
                return False
            if i == 0:
                return frog_jump(1, binary_search(i+1, 1))
            else:
                return frog_jump(k-1, binary_search(i+1, stones[i] + (k-1))) or frog_jump(k+1, binary_search(i+1, stones[i] + (k+1))) or frog_jump(k, binary_search(i+1, stones[i] + (k)))
        return frog_jump(1,0)
   

