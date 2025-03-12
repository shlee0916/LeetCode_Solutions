'''
https://leetcode.com/problems/sliding-window-maximum/description/
'''

from collections import deque

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        que = deque()

        for idx in range(len(nums)):

            if que and idx - que[0] == k:
                que.popleft()

            while que:
                if nums[que[-1]] < nums[idx]:
                    que.pop()
                else:
                    break

            que.append(idx)

            if idx >= k - 1:
                ans.append(nums[que[0]])

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxSlidingWindow(nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3)
    assert test1 == [3, 3, 5, 5, 6, 7]

    test2 = sol.maxSlidingWindow(nums = [1], k = 1)
    assert test2 == [1]
    