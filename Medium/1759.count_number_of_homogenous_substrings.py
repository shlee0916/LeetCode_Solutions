'''
https://leetcode.com/problems/count-number-of-homogenous-substrings/description/?envType=daily-question&envId=2023-11-09
'''

class Solution:
    def countHomogenous(self, s: str) -> int:
        cur_ch = s[0]
        cnt = 1
        res = 1

        for ch in s[1:]:
            if ch == cur_ch:
                cnt += 1
                cur_ch = ch
            else:
                cnt = 1
                cur_ch = ch

            res += cnt

        return res % ((10 ** 9) + 7)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countHomogenous(s = "abbcccaa")
    assert test1 == 13

    test2 = sol.countHomogenous(s = "xy")
    assert test2 == 2

    test3 = sol.countHomogenous(s = "zzzzz")
    assert test3 == 15
    