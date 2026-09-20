import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        rnums = []
        if 0 not in nums:
            prodnum = math.prod(nums)
            for i in nums:
                rnums.append(prodnum // i)
        else:
            for i in nums:
                cnums = nums.copy()
                cnums.remove(i)
                rnums.append(math.prod(cnums))
        return rnums
    
# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         returnnums = [1]
#         rnums = 1
#         i = 1
#         while i < len(nums):
#             returnnums.append(returnnums[i-1] * nums[i-1])
#             i += 1
#         j = len(nums) - 2
#         while j >= 0:
#             rnums *= nums[j+1]
#             returnnums[j] = returnnums[j] * rnums
#             j -= 1
#         return returnnums
        