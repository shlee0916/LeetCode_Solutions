'''
https://leetcode.com/problems/decode-string/description/
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0

        for ch in s:
            if ch == "[":
                stack.append(cur_str)
                stack.append(cur_num)

                cur_str = ""
                cur_num = 0

            elif ch == "]":
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + num * cur_str

            elif ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
                
            else:
                cur_str += ch

        return cur_str


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.decodeString(s = "3[a]2[bc]")
    assert test1 == "aaabcbc"
    
    test2 = sol.decodeString(s = "3[a2[c]]")
    assert test2 == "accaccacc"
    
    test3 = sol.decodeString(s = "2[abc]3[cd]ef")
    assert test3 == "abcabccdcdcdef"
    