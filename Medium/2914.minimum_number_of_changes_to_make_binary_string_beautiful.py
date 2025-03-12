'''
https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2024-11-05
'''

class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        parts = [s[idx : idx + 2] for idx in range(0, len(s) - 1, 2)]
        
        for part in parts:
            if part[0] != part[1]:
                ans += 1

        return ans
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minChanges(s = "1001")
    assert test1 == 2

    test2 = sol.minChanges(s = "10")
    assert test2 == 1

    test3 = sol.minChanges(s = "0000")
    assert test3 == 0
    