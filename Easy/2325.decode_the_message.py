'''
https://leetcode.com/problems/decode-the-message/description/
'''

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_table = {" ": " "}
        ascii_code = 97

        for ch in key:
            if ch not in key_table and ch != " ":
                key_table[ch] = chr(ascii_code)
                ascii_code += 1

        return "".join(key_table[msg] for msg in message)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")
    assert test1 == "this is a secret"
    
    test2 = sol.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
    assert test2 == "the five boxing wizards jump quickly"
    