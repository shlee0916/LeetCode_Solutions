'''
https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/
'''

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)

        stack = []
        for idx, value in enumerate(heights):
            while stack and heights[stack[-1]] <= value:
                ans[stack.pop()] += 1
            if stack:
                ans[stack[-1]] += 1

            stack.append(idx)

        return ans
            

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.canSeePersonsCount(heights = [10, 6, 8, 5, 11, 9])
    assert test1 == [3, 1, 2, 1, 1, 0]
    
    test2 = sol.canSeePersonsCount(heights = [5, 1, 2, 3, 10])
    assert test2 == [4, 1, 1, 1, 0]
    