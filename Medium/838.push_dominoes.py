'''
https://leetcode.com/problems/push-dominoes/description/?envType=daily-question&envId=2025-05-02
'''

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        new_s = "L" + dominoes + "R"
        ans = ""
        prev = 0
        for cur in range(1, len(new_s)):
            if new_s[cur] == ".":
                continue

            win = cur - prev - 1
            if prev > 0:
                ans += new_s[prev]

            if new_s[cur] == new_s[prev]:
                ans += new_s[cur] * win

            elif new_s[cur] == "R" and new_s[prev] == "L":
                ans += "." * win

            else:
                ans += "R" * (win // 2) + "." * (win % 2) + "L" * (win // 2)

            prev = cur

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.pushDominoes(dominoes = "RR.L")
    assert test1 == "RR.L"

    test2 = sol.pushDominoes(dominoes = ".L.R...LR..L..")
    assert test2 == "LL.RR.LLRRLL.."
    