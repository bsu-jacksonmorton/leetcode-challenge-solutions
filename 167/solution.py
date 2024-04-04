class Solution:
    '''
    Runtime: O(n)
    Space: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while (total := numbers[low] + numbers[high]) != target:
            if total > target:
                high -= 1
            else:
                low += 1
        return [low+1, high+1]
