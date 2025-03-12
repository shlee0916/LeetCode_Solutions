'''
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/?envType=daily-question&envId=2025-02-25
'''

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = even = 0
        res = 0
        
        for num in arr:
            even += 1
            if num % 2:
                odd, even = even, odd

            res = (res + odd) % (10 ** 9 + 7)

        return res
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numOfSubarrays(arr = [1, 3, 5])
    assert test1 == 4

    test2 = sol.numOfSubarrays(arr = [2, 4, 6])
    assert test2 == 0

    test3 = sol.numOfSubarrays(arr = [1, 2, 3, 4, 5, 6, 7])
    assert test3 == 16
    