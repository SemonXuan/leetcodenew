'''
Author: Semon
Date: 2026-09-26 21:02:42
LastEditors: Semon
LastEditTime: 2026-09-26 21:02:54
Description: 
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            point = t.find(i)
            if point == -1:
                return False
            else:
                t = t[point+1:]
        return True
    

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if s == "":
#             return True
#         point = 0
#         for i in t:
#             if s[point] == i:
#                 point += 1
#             if point == len(s):
#                 return True
#         return False

        