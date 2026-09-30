'''
Author: Semon
Date: 2026-09-30 20:45:15
LastEditors: Semon
LastEditTime: 2026-09-30 20:45:24
Description: 
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max_vowel = sum(1 for c in s[0:k] if c in vowels)
        point_vowel = max_vowel
        for i in range(1, len(s)-k+1):
            if s[i-1] in vowels:
                point_vowel -= 1
            if s[i+k-1] in vowels:
                point_vowel += 1
            if point_vowel > max_vowel:
                max_vowel = point_vowel
            if max_vowel == k:
                return k
        return max_vowel

        