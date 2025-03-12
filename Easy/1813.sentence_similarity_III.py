'''
https://leetcode.com/problems/sentence-similarity-iii/?envType=daily-question&envId=2025-03-03
'''

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1_words = sentence1.split()
        s2_words = sentence2.split()

        if len(s1_words) > len(s2_words):
            s1_words, s2_words = s2_words, s1_words

        while s1_words:
            if s1_words[0] == s2_words[0]:
                s1_words.pop(0)
                s2_words.pop(0)

            elif s1_words[-1] == s2_words[-1]:
                s1_words.pop()
                s2_words.pop()

            else:
                return False

        return True
        

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley")
    assert test1 == True
    
    test2 = sol.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words")
    assert test2 == False
    
    test3 = sol.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating")
    assert test3 == True
    