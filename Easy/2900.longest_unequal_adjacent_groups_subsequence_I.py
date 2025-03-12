'''
https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/
'''

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        prev = groups[0]

        for idx in range(1, len(words)):
            if groups[idx] != prev:
                ans.append(words[idx])
                prev = groups[idx]
        
        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getLongestSubsequence(words = ["e", "a", "b"], groups = [0, 0, 1])
    assert test1 == ["e", "b"]

    test2 = sol.getLongestSubsequence(words = ["a", "b", "c", "d"], groups = [1, 0, 1, 1])
    assert test2 == ["a", "b", "c"]
    