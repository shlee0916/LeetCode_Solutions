'''
https://leetcode.com/problems/longest-common-subsequence/description/
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lengths = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for idx1, ch1 in enumerate(text1):
            for idx2, ch2 in enumerate(text2):
                if ch1 == ch2:
                    lengths[idx1 + 1][idx2 + 1] = 1 + lengths[idx1][idx2]
                else:
                    lengths[idx1 + 1][idx2 + 1] = max(lengths[idx1][idx2 + 1], lengths[idx1 + 1][idx2])

        return lengths[-1][-1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestCommonSubsequence("abcde", "ace")
    print(test1, 3)
    assert test1 == 3

    test2 = sol.longestCommonSubsequence("abc", "abc")
    print(test2, 3)
    assert test2 == 3

    test3 = sol.longestCommonSubsequence("abc", "def")
    print(test3, 0)
    assert test3 == 0

    test4 = sol.longestCommonSubsequence("abcba", "abcbcba")
    print(test4, 5)
    assert test4 == 5
