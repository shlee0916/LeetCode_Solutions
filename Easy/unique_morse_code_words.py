'''
https://leetcode.com/problems/unique-morse-code-words/
'''
class Solution(object):
    morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_words = set()
        
        for word in words:
            morses = ""
            for char in word:
                morses += self.morse_codes[ord(char) - 97]
                
            morse_words.add(morses)
            
        return len(morse_words)
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.uniqueMorseRepresentations(["gin","zen","gig","msg"]), 2)