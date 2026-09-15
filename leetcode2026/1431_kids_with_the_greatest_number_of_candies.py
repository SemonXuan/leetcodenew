'''
Author: Semon
Date: 2026-09-15 20:29:57
LastEditors: Semon
LastEditTime: 2026-09-15 20:33:43
Description: 
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        return [i + extraCandies >= maxcandies for i in candies]
        