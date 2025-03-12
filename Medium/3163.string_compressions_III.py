'''
https://leetcode.com/problems/string-compression-iii/?envType=daily-question&envId=2024-11-04
'''

class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        cur_ch = word[0]
        cur_num = 1
        for ch in word[1:]:
            if cur_ch == ch and cur_num < 9:
                cur_num += 1
            else:
                ans += f"{cur_num}{cur_ch}"
                cur_ch = ch
                cur_num = 1

        ans += f"{cur_num}{cur_ch}"

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.compressedString(word = "abcde")
    assert test1 == "1a1b1c1d1e"

    test2 = sol.compressedString(word = "aaaaaaaaaaaaaabb")
    assert test2 == "9a5a2b"
    