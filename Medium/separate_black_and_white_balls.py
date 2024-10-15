'''
https://leetcode.com/problems/separate-black-and-white-balls/description/?envType=daily-question&envId=2024-10-15
'''

class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cnt = 0
        for ch in s:
            if ch == "0":
                ans += cnt
            else:
                cnt += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minimumSteps(s = "101")
    assert test1 == 1

    test2 = sol.minimumSteps(s = "100")
    assert test2 == 2

    test3 = sol.minimumSteps(s = "0111")
    assert test3 == 0
    