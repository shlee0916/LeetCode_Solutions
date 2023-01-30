'''
https://leetcode.com/problems/palindrome-partitioning/description/
'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        for idx in range(1, len(s) + 1):
            if s[:idx] == s[idx - 1::-1]:
                for rest in self.partition(s[idx:]):
                    res.append([s[:idx]] + rest)

        return res if res else [[]]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.partition("aab")
    print(test1, [["a", "a", "b"], ["aa", "b"]])
    assert test1 == [["a", "a", "b"], ["aa", "b"]]

    test2 = sol.partition("a")
    print(test2, [["a"]])
    assert test2 == [["a"]]
    