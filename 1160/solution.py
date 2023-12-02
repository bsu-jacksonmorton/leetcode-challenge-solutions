class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        characters = dict(Counter(chars))
        res = 0
        for word in words:
            if len(word) > len(chars):
                continue
            characters_copy = characters.copy()
            ok = True
            for char in word:
                if char not in characters_copy or characters_copy[char] == 0:
                    ok = False
                    break
                else:
                    characters_copy[char] -= 1
            if ok:
                res += len(word)
        return res
