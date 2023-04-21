'''
https://leetcode.com/problems/queue-reconstruction-by-height/description/
'''

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key = lambda x: (-x[0], x[1]))

        result = []
        for person in sorted_people:
            result.insert(person[1], person)

        return result
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.reconstructQueue(people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    assert test1 == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

    test2 = sol.reconstructQueue(people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]])
    assert test2 == [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]
