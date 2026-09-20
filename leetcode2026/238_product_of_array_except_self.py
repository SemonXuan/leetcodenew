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
#         result = [1]
#         rnums = 1
#         for i in range(1, len(nums)):
#             result.append(result[i-1] * nums[i-1])
#         j = len(nums) - 2
#         for j in range(len(nums)-2, -1, -1):
#             rnums = rnums * nums[j+1]
#             result[j] = result[j] * rnums
#         return result
        
        