'''
https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
'''

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)

        ans = [0] * 10
        ans[0] = cnt["z"]
        ans[2] = cnt["w"]
        ans[4] = cnt["u"]
        ans[6] = cnt["x"]
        ans[8] = cnt["g"]

        ans[1] = cnt["o"] - ans[0] - ans[2] - ans[4]
        ans[3] = cnt["h"] - ans[8]
        ans[5] = cnt["f"] - ans[4]
        ans[7] = cnt["s"] - ans[6]
        ans[9] = cnt["i"] - ans[6] - ans[5] - ans[8]

        return "".join(str(num) * freq for num, freq in enumerate(ans))


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.originalDigits(s = "owoztneoer")
    assert test1 == "012"
    
    test2 = sol.originalDigits(s = "fviefuro")
    assert test2 == "45"
    