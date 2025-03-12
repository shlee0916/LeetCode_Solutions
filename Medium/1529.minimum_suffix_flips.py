'''
https://leetcode.com/problems/minimum-suffix-flips/description/
'''

class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        cur_num = "0"
        for num in target:
            if num != cur_num:
                ans += 1
                cur_num = "0" if cur_num == "1" else "1"

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minFlips(target = "10111")
    assert test1 == 3
    
    test2 = sol.minFlips(target = "101")
    assert test2 == 3
    
    test3 = sol.minFlips(target = "00000")
    assert test3 == 0
    