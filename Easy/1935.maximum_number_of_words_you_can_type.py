'''
https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15
'''

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        broken_set = set(brokenLetters)
        for word in text.split():
            if len(set(word).intersection(broken_set)) == 0:
                ans += 1

        return ans
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.canBeTypedWords(text = "hello world", brokenLetters = "ad")
    assert test1 == 1

    test2 = sol.canBeTypedWords(text = "leet code", brokenLetters = "lt")
    assert test2 == 1

    test3 = sol.canBeTypedWords(text = "leet code", brokenLetters = "e")
    assert test3 == 0
    