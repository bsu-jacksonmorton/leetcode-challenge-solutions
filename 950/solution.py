class Solution:
    '''
    simulation method
    runtime: O(nlogn)
    space: O(n)
    '''
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [None] * len(deck)
        q = [i for i in range(len(deck))]
        while q:
            index = q.pop(0)
            ans[index] = deck.pop(0)
            if not q:
                break
            q.append(q.pop(0))
        return ans
