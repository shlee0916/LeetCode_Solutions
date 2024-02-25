'''
https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2024-02-24
'''

from collections import defaultdict, deque
from itertools import groupby

from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knowing_secret = set({0, firstPerson})
        for _, meeting in groupby(sorted(meetings, key = lambda x: x[2]), key = lambda x: x[2]):
            que = set()
            graph = defaultdict(list)

            for person_, person__, _ in meeting:
                graph[person_].append(person__)
                graph[person__].append(person_)

                if person_ in knowing_secret:
                    que.add(person_)
                if person__ in knowing_secret:
                    que.add(person__)

            que = deque(que)
            while que:
                person = que.popleft()
                for met_person in graph[person]:
                    if met_person not in knowing_secret:
                        knowing_secret.add(met_person)
                        que.append(met_person)
            
        return knowing_secret


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findAllPeople(n = 6, meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson = 1)
    assert list(test1) == [0, 1, 2, 3, 5]
    
    test2 = sol.findAllPeople(n = 4, meetings = [[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson = 3)
    assert list(test2) == [0, 1, 3]
    
    test3 = sol.findAllPeople(n = 5, meetings = [[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson = 1)
    assert list(test3) == [0, 1, 2, 3, 4]
    