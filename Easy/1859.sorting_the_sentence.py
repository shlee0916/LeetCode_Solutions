'''
https://leetcode.com/problems/sorting-the-sentence/description/
'''

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key = lambda x: x[-1])
        words = [word[:-1] for word in words]

        return " ".join(words)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sortSentence(s = "is2 sentence4 This1 a3")
    assert test1 == "This is a sentence"
    
    test2 = sol.sortSentence(s = "Myself2 Me1 I4 and3")
    assert test2 == "Me Myself and I"
    