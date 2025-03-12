'''
https://leetcode.com/problems/word-pattern/description/
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        patterns = {}

        if len(pattern) != len(words):
            return False

        if len(set(pattern)) != len(set(words)):
            return False

        for word, p in zip(words, pattern):
            if word not in patterns:
                patterns[word] = p
            elif patterns[word] != p:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.wordPattern(pattern = "abba", s = "dog cat cat dog")
    print(test1, True)
    assert test1 == True
    
    test2 = sol.wordPattern(pattern = "abba", s = "dog cat cat fish")
    print(test2, False)
    assert test2 == False
    
    test3 = sol.wordPattern(pattern = "aaaa", s = "dog cat cat dog")
    print(test3, False)
    assert test3 == False
    