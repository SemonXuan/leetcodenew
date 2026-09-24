'''
Author: Semon
Date: 2026-09-24 19:47:03
LastEditors: Semon
LastEditTime: 2026-09-24 19:47:08
Description: 
'''
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.remove(nums[i])
                point += 1
        nums += [0] * point  