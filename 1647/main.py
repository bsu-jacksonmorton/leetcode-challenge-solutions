class Solution:
    def minDeletions(self, s: str) -> int:
        """
        This solution uses a greedy approach. Using a greedy approach wasn't my initial idea
        but after reading the discussion boards I thought I would give it a try. I was under the impression that frequencies would need to be sorted in descending order and that was my original approach but it turns out that it doesn't really matter.
        """
        res = 0
        frequencies = Counter(s)
        seen = set()
        for frequency in list(frequencies.values()):
            if frequency not in seen:
                seen.add(frequency)
                continue
            while frequency > 0 and frequency in seen:
                frequency -= 1
                res += 1
            if frequency > 0:
                seen.add(frequency)
        return res
