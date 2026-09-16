class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            leftpoint = (i == 0) or flowerbed[i-1] == 0
            rightpoint = (i == len(flowerbed) - 1) or flowerbed[i+1] == 0
            if leftpoint and rightpoint and flowerbed[i] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n
    

# class Solution:
#     def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
#         zflower, nflower = 0, 0
#         isfirst = flowerbed[0]
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0:
#                 zflower += 1
#             elif zflower > 0:
#                 if isfirst:
#                     nflower += (zflower - 1) // 2
#                 else:
#                     nflower += zflower // 2
#                 isfirst = flowerbed[i]
#                 zflower = 0
#         if sum(flowerbed) == 0:
#             nflower += (zflower + 1) // 2
#         elif flowerbed[-1] == 0:
#                 nflower += zflower // 2
#         return nflower >= n