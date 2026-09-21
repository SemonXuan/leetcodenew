'''
Author: Semon
Date: 2026-09-21 20:34:47
LastEditors: Semon
LastEditTime: 2026-09-21 20:42:40
Description: 
'''

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

        