'''
https://leetcode.com/problems/shuffle-string/description/
'''

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_arr = []
        for ch, idx in zip([ch for ch in s], indices):
            new_arr.append((ch, idx))

        new_arr.sort(key = lambda x: x[1])

        return "".join([ch for ch, _ in new_arr])


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.restoreString(s = "codeleet", indices = [4, 5, 6, 7, 0, 2, 1, 3])
    assert test1 == "leetcode"
    
    test2 = sol.restoreString(s = "abc", indices = [0, 1, 2])
    assert test2 == "abc"
    