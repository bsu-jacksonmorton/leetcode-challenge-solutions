class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1Ptr = 0
        word2Ptr = 0
        string1Ptr = 0
        string2Ptr = 0
        while word1[word1Ptr][string1Ptr] == word2[word2Ptr][string2Ptr]:
            string1Ptr += 1
            string2Ptr += 1
            # check to see if we need to update our current word pointers
            if string1Ptr >= len(word1[word1Ptr]):
                word1Ptr += 1
                string1Ptr = 0
            if string2Ptr >= len(word2[word2Ptr]):
                word2Ptr += 1
                string2Ptr = 0
            # check if we have iterated through all of the words
            if word1Ptr >= len(word1) or word2Ptr >= len(word2):
                break
        return word1Ptr == len(word1) and word2Ptr == len(word2)
