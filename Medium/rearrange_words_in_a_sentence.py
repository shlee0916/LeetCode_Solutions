'''
https://leetcode.com/problems/rearrange-words-in-a-sentence/description/
'''

class Solution:
    def arrangeWords(self, text: str) -> str:
        words = [word.lower() for word in text.split()]
        words.sort(key = lambda word: len(word))
        words[0] = words[0].capitalize()

        return " ".join(words)
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.arrangeWords(text = "Leetcode is cool")
    assert test1 == "Is cool leetcode"
    
    test2 = sol.arrangeWords(text = "Keep calm and code on")
    assert test2 == "On and keep calm code"
    
    test3 = sol.arrangeWords(text = "To be or not to be")
    assert test3 == "To be or to be not"
    