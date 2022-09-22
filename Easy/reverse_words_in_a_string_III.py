'''
https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([sub_s[::-1] for sub_s in s.split(" ")])
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
    print(sol.reverseWords("God Ding"), "doG gniD")