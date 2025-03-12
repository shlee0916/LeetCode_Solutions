'''
https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2023-12-22
'''

class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == "0" else 0
        ones = s.count("1", 1)

        ans = zeros + ones
        for idx in range(1, len(s) - 1):
            if s[idx] == "0":
                zeros += 1
            else:
                ones -= 1

            ans = max(zeros + ones, ans)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxScore(s = "011101")
    assert test1 == 5
    
    test2 = sol.maxScore(s = "00111")
    assert test2 == 5
    
    test3 = sol.maxScore(s = "1111")
    assert test3 == 3
    