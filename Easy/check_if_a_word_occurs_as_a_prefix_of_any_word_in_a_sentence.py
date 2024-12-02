'''
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/?envType=daily-question&envId=2024-12-02
'''

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        for idx, word in enumerate(words):
            if word.startswith(searchWord):
                return idx + 1

        return -1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg")
    assert test1 == 4

    test2 = sol.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro")
    assert test2 == 2

    test3 = sol.isPrefixOfWord(sentence = "i am tired", searchWord = "you")
    assert test3 == -1
    