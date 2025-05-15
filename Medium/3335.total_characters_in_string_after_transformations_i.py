'''
https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/?source=submission-noac
'''

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        ans = [0] * 26

        for ch in s:
            ans[ord(ch) - ord('a')] += 1

        for _ in range(t):
            tmp = [0] * 26
            for idx in range(25):
                tmp[idx + 1] = ans[idx] % MOD

            tmp[0] = (tmp[0] + ans[25]) % MOD
            tmp[1] = (tmp[1] + ans[25]) % MOD

            ans = tmp

        return sum(ans) % MOD


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.lengthAfterTransformations(s = "abcyy", t = 2)
    assert test1 == 7

    test2 = sol.lengthAfterTransformations(s = "azbk", t = 1)
    assert test2 == 5
    