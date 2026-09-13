class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        leni = min(len(word1),len(word2))
        for i in range(leni):
            merged.append(word1[i] + word2[i])
        merged.append(word1[leni:] + word2[leni:])
        return ''.join(merged)

# 方法二：
# merged = [i+j for i,j in zip(test1, test2)]
# print(''.join(merged) + test1[len(merged):] + test2[len(merged):])

# 方法三：
# print(''.join([i+j for i,j in zip_longest(test1, test2, fillvalue='')]))