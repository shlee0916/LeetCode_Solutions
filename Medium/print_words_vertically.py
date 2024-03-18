'''
https://leetcode.com/problems/print-words-vertically/
'''

from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        word_max_len = max(len(word) for word in words)
        words = [word.ljust(word_max_len) for word in words]
        words = ["".join(new_word) for new_word in zip(*words)]

        return [word.rstrip() for word in words]
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.printVertically(s = "HOW ARE YOU")
    assert test1 == ["HAY", "ORO", "WEU"]
    
    test2 = sol.printVertically(s = "TO BE OR NOT TO BE")
    assert test2 == ["TBONTB", "OEROOE", "   T"]

    test3 = sol.printVertically(s = "CONTEST IS COMING")
    assert test3 == ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]
    