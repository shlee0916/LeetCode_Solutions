'''
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
'''

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        return len(set(Counter(s).values())) == 1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.areOccurrencesEqual(s = "abacbc")
    assert test1 == True

    test2 = sol.areOccurrencesEqual(s = "aaabb")
    assert test2 == False
    