'''
https://leetcode.com/problems/partition-array-for-maximum-sum/
'''

from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        length = len(arr)
        maximums = [0] * length

        for idx in range(k):
            maximums[idx] = max(arr[:idx + 1]) * (idx + 1)

        for arr_idx in range(k, length):
            cur_maxes = []

            for k_idx in range(k):
                cur_maxes.append(maximums[arr_idx - k_idx - 1] + max(arr[(arr_idx - k_idx) : (arr_idx + 1)]) * (k_idx + 1))

            maximums[arr_idx] = max(cur_maxes)

        return maximums[-1]
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxSumAfterPartitioning(arr = [1, 15, 7, 9, 2, 5, 10], k = 3)
    print(test1, 84)
    assert test1 == 84

    test2 = sol.maxSumAfterPartitioning(arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k = 4)
    print(test2, 83)
    assert test2 == 83

    test3 = sol.maxSumAfterPartitioning(arr = [1], k = 1)
    print(test3, 1)
    assert test3 == 1
    