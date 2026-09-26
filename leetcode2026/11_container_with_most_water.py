'''
Author: Semon
Date: 2026-09-26 21:31:09
LastEditors: Semon
LastEditTime: 2026-09-26 21:31:14
Description: 
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        left, right = 0, len(height)-1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > maxarea:
                maxarea = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

        