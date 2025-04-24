'''
https://leetcode.com/problems/count-good-triplets/?envType=daily-question&envId=2025-04-14
'''

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        length = len(arr)

        for a_idx in range(length):
            for b_idx in range(a_idx + 1, length):
                 if abs(arr[a_idx] - arr[b_idx]) <= a:
                    for c_idx in range(b_idx + 1, length):
                        if abs(arr[b_idx] - arr[c_idx]) <= b and abs(arr[c_idx] - arr[a_idx]) <= c:
                            ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countGoodTriplets(arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3)
    assert test1 == 4

    test2 = sol.countGoodTriplets(arr = [1, 1, 2, 2, 3], a = 0, b = 0, c = 1)
    assert test2 == 0
    