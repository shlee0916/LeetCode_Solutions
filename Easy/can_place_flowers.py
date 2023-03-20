'''
https://leetcode.com/problems/can-place-flowers/description/
'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed) - 1
        planted = 0
        for idx, plant in enumerate(flowerbed):
            if (plant == 0 and 
            (idx == 0 or flowerbed[idx - 1] == 0) and 
            (idx == flowerbed_len or flowerbed[idx + 1] == 0)):
                planted += 1
                flowerbed[idx] = 1

        return planted >= n
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.canPlaceFlowers(flowerbed = [1, 0, 0, 0, 1], n = 1)
    print(test1, True)
    assert test1 == True

    test2 = sol.canPlaceFlowers(flowerbed = [1, 0, 0, 0, 1], n = 2)
    print(test2, False)
    assert test2 == False
    