'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
from typing import List


class Solution:
    def __init__(self):
        self.num_alpha = {"2": ("a", "b", "c"),
                         "3": ("d", "e", "f"),
                         "4": ("g", "h", "i"),
                         "5": ("j", "k", "l"),
                         "6": ("m", "n", "o"),
                         "7": ("p", "q", "r", "s"),
                         "8": ("t", "u", "v"),
                         "9": ("w", "x", "y", "z")}
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        for num in digits:
            if not result:
                result = [alpha for alpha in self.num_alpha[num]]
            else:
                tmp_alpha = []
                for re_str in result:
                    for add_str in self.num_alpha[num]:
                        tmp_alpha.append(re_str + add_str)
                result = tmp_alpha
                
        return result
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
    print(sol.letterCombinations(""), [])
    print(sol.letterCombinations("2"), ["a", "b", "c"])