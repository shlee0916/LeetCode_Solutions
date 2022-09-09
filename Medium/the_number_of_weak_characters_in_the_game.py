'''
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
'''
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))
        
        you_weak = 0
        max_defense = properties[0][1]
        for _, cur_def in properties[1:]:
            if cur_def < max_defense:
                you_weak += 1
                
            max_defense = max(cur_def, max_defense)
                    
        return you_weak


if __name__ == "__main__":
    sol = Solution()

    testcase1 = [[5,5],[6,3],[3,6]]
    testcase2 = [[2,2],[3,3]]
    testcase3 = [[1,5],[10,4],[4,3]]

    print(sol.numberOfWeakCharacters(testcase1), 0)
    print(sol.numberOfWeakCharacters(testcase2), 1)
    print(sol.numberOfWeakCharacters(testcase3), 1)