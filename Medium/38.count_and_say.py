'''
https://leetcode.com/problems/count-and-say/submissions/1610088219/?envType=daily-question&envId=2025-04-18
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for _ in range(n - 1):
            num = ans[0]
            temp = ""
            cnt = 0
            for ch in ans:
                if num == ch:
                    cnt += 1
                else:
                    temp += str(cnt) + num
                    cnt = 1
                    num = ch
            temp += str(cnt) + num
            ans = temp

        return ans
            
            
if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countAndSay(4)
    assert test1 == "1211"

    test2 = sol.countAndSay(1)
    assert test2 == "1"
