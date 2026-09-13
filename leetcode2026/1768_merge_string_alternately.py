class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        leni = min(len(word1),len(word2))
        for i in range(leni):
            merged += word1[i] + word2[i]
        merged += word1[leni:] + word2[leni:]
        return merged
