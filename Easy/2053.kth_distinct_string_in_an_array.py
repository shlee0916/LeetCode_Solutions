'''
https://leetcode.com/problems/kth-distinct-string-in-an-array/?envType=daily-question&envId=2024-08-05
'''

from collections import Counter

from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_map = Counter(arr)
        str_map = [string for string, val in str_map.items() if val == 1]

        if len(str_map) < k:
            return ""

        else:
            return str_map[k - 1]
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.kthDistinct(arr = ["d", "b", "c", "b", "c", "a"], k = 2)
    assert test1 == "a"

    test2 = sol.kthDistinct(arr = ["aaa", "aa", "a"], k = 1)
    assert test2 == "aaa"

    test3 = sol.kthDistinct(arr = ["a", "b", "a"], k = 3)
    assert test3 == ""
    