'''
https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
'''

from collections import deque

from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avgs = []

        que = deque(sorted(nums))
        for _ in range(len(nums) // 2):
            avgs.append((que.popleft() + que.pop()) / 2) 

        return min(avgs)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumAverage(nums = [7, 8, 3, 4, 15, 13, 4, 1])
    assert test1 == 5.5

    test2 = sol.minimumAverage(nums = [1, 9, 8, 3, 10, 5])
    assert test2 == 5.5

    test3 = sol.minimumAverage(nums = [1, 2, 3, 7, 8, 9])
    assert test3 == 5.0
    