'''
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
'''

from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)

        for person, size in enumerate(groupSizes):
            groups[size].append(person)

        result = []
        for size, people in groups.items():
            for idx in range(len(people) // size):
                result.append(people[size * idx : size * (idx + 1)])

        return result


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.groupThePeople(groupSizes = [3, 3, 3, 3, 3, 1, 3])
    assert set(tuple(ele) for ele in test1) == set(tuple(ele) for ele in [[5], [0, 1, 2], [3, 4, 6]])

    test2 = sol.groupThePeople(groupSizes = [2, 1, 3, 3, 3, 2])
    assert set(tuple(ele) for ele in test2) == set(tuple(ele) for ele in [[1], [0, 5], [2, 3, 4]])
