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