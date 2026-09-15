'''
Author: Semon
Date: 2026-09-15 18:44:34
LastEditors: Semon
LastEditTime: 2026-09-15 18:44:42
Description: 
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        while len1 % len2 != 0:
            len1, len2 = len2, len1 % len2
        strx = str2[:len2]
        if "".join(str1.split(strx)) == "" and "".join(str2.split(strx)) == "":
            return str1[:len2] 
        else:
            return ""

        # if str1 + str2 != str2 + str1:
        #     return ""

        # maxlen = gcd(len(str1), len(str2))
        # return str1[:maxlen]