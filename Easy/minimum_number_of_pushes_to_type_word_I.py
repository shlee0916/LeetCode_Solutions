'''
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/
'''

class Solution:
    def minimumPushes(self, word: str) -> int:
        share, remainder = divmod(len(word), 8)

        return 4 * share * (share + 1) + remainder * (share + 1)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumPushes(word = "abcde")
    assert test1 == 5
    
    test2 = sol.minimumPushes(word = "xycdefghij")
    assert test2 == 12
    