class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + target]:
                return arr[i]
