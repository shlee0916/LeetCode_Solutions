'''
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/?envType=daily-question&envId=2023-12-30
'''

from collections import Counter

from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        all_chs = Counter("".join(words))

        for num_ch in all_chs.values():
            if num_ch % len(words) != 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.makeEqual(words = ["abc", "aabc", "bc"])
    assert test1 == True
    
    test2 = sol.makeEqual(words = ["ab", "a"])
    assert test2 == False
    