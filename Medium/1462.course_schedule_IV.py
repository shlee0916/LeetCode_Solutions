'''
https://leetcode.com/problems/course-schedule-iv/?envType=daily-question&envId=2025-01-27
'''

from collections import defaultdict, deque

from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_map = defaultdict(list)
        for pre, cur in prerequisites:
            course_map[pre].append(cur)

        ans = []
        for start, end in queries:
            stack = deque([start])
            visit = set()
            while stack:
                if end in stack:
                    ans.append(True)
                    break
                
                for _ in range(len(stack)):
                    cur_node = stack.popleft()
                    visit.add(cur_node)

                    for next_node in course_map[cur_node]:
                        if next_node not in visit:
                            stack.append(next_node)

            if not stack:
                ans.append(False)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.checkIfPrerequisite(numCourses = 2, prerequisites = [[1, 0]], queries = [[0, 1], [1, 0]])
    assert test1 == [False, True]

    test2 = sol.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1, 0], [0, 1]])
    assert test2 == [False, False]

    test3 = sol.checkIfPrerequisite(numCourses = 3, prerequisites = [[1, 2], [1, 0], [2, 0]], queries = [[1, 0], [1, 2]])
    assert test3 == [True, True]
    