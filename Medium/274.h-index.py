'''
https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_cit = sorted(citations)[::-1]

        ans = 0
        for idx, num in enumerate(sorted_cit):
            if num > idx:
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.hIndex(citations = [3, 0, 6, 1, 5])
    assert test1 == 3

    test2 = sol.hIndex(citations = [1, 3, 1])
    assert test2 == 1

    test3 = sol.hIndex(citations = [100])
    assert test3 == 1

    test4 = sol.hIndex(citations = [4, 4, 0, 0])
    assert test4 == 2
    