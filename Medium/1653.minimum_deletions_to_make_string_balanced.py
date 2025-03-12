'''
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2024-07-31
'''

class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_cnt = 0
        ans = [0]

        for ch in s:
            if ch == "b":
                b_cnt += 1
                ans.append(ans[-1])
            else:
                ans.append(min(ans[-1] + 1, b_cnt))

        return ans[-1]
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumDeletions(s = "aababbab")
    assert test1 == 2

    test2 = sol.minimumDeletions(s = "bbaaaaabb")
    assert test2 == 2
