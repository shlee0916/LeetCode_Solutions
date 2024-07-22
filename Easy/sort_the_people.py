'''
https://leetcode.com/problems/sort-the-people/?envType=daily-question&envId=2024-07-22
'''

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        sorted_people = sorted(list(zip(heights, names)), key = lambda x: x[0], reverse = True)

        return [name for _, name in sorted_people]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.sortPeople(names = ["Mary", "John", "Emma"], heights = [180, 165, 170])
    assert test1 == ["Mary", "Emma", "John"]

    test2 = sol.sortPeople(names = ["Alice", "Bob", "Bob"], heights = [155, 185, 150])
    assert test2 == ["Bob", "Alice", "Bob"]
    