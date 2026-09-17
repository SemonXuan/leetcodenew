'''
Author: Semon
Date: 2026-09-17 19:25:05
LastEditors: Semon
LastEditTime: 2026-09-17 19:25:12
Description: 
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        i, j = 0, len(arr) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while i < j:
            if arr[i] not in vowels:
                i += 1
            if arr[j] not in vowels:
                j -= 1
            if arr[i] in vowels and arr[j] in vowels:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return "".join(arr)
        