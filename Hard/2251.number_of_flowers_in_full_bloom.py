'''
https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/?envType=daily-question&envId=2023-10-11
'''

from bisect import bisect_right, bisect_left

from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start, end = map(sorted, zip(*flowers))
        ans = []

        for person in people:
            ans.append(bisect_right(start, person) - bisect_left(end, person))

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.fullBloomFlowers(flowers = [[1, 6], [3, 7], [9, 12], [4, 13]], people = [2, 3, 7, 11])
    assert test1 == [1, 2, 2, 2]

    test2 = sol.fullBloomFlowers(flowers = [[1, 10], [3, 3]], people = [3, 3, 2])
    assert test2 == [2, 2, 1]
