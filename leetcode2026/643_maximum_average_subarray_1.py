'''
Author: Semon
Date: 2026-09-28 20:35:29
LastEditors: Semon
LastEditTime: 2026-09-28 20:35:35
Description: 
'''
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        rec_sum = sum(nums[:k])
        max_sum = rec_sum
        i = 0
        while i < len(nums)-k:
            rec_sum = rec_sum - nums[i] + nums[i+k]
            if rec_sum > max_sum:
                max_sum = rec_sum
            i += 1
        return max_sum / k       