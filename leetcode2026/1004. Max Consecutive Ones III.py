'''
Author: Semon
Date: 2026-09-30 21:07:25
LastEditors: Semon
LastEditTime: 2026-09-30 21:07:32
Description: 
'''
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
        return len(nums) - left

        