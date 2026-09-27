'''
Author: Semon
Date: 2026-09-27 21:32:14
LastEditors: Semon
LastEditTime: 2026-09-27 21:32:18
Description: 
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        left, right = 0, len(nums)-1
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                left += 1
                right -= 1
                result += 1
            elif s < k:
                left += 1
            else:
                right -= 1
        return result
        
        