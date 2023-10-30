'''
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2023-10-30
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count(num):
            cnt = 0 
            while num:
                num &= num - 1
                cnt += 1

            return cnt

        temp = []
        for num in arr:
            heappush(temp, (count(num), num))

        ans = []
        while temp:
            ans.append(heappop(temp)[1])

        return ans
        

if __name__  == "__main__":
    sol = Solution()

    test1 = sol.sortByBits(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8])
    assert test1 == [0, 1, 2, 4, 8, 3, 5, 6, 7]
    
    test2 = sol.sortByBits(arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
    assert test2 == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
