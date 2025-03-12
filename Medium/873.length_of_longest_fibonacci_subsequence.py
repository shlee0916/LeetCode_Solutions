'''
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/?envType=daily-question&envId=2025-02-27
'''

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        length = len(arr)
        dp = [[0] * length for _ in range(length)]

        num_idx = {num: idx for idx, num in enumerate(arr)}
        ans = 0
        for cur in range(length):
            for prev in range(cur):
                diff = arr[cur] - arr[prev]
                prev_idx = num_idx.get(diff, -1)

                if diff < arr[prev] and prev_idx >= 0:
                    dp[prev][cur] = dp[prev_idx][prev] + 1
                else:
                    dp[prev][cur] = 2

                ans = max(ans, dp[prev][cur])

        return ans if ans > 2 else 0


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.lenLongestFibSubseq(arr = [1, 2, 3, 4, 5, 6, 7, 8])
    assert test1 == 5

    test2 = sol.lenLongestFibSubseq(arr = [1, 3, 7, 11, 12, 14, 18])
    assert test2 == 3
    