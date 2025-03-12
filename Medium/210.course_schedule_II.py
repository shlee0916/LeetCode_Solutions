'''
https://leetcode.com/problems/course-schedule-ii/description/
'''
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        pre_nums = defaultdict(int)
        que = []
        ans = []

        for course, pre in prerequisites:
            courses[pre].append(course)
            pre_nums[course] += 1

        for course_num in range(numCourses):
            if pre_nums[course_num] == 0:
                que.append(course_num)

        while que:
            cur_course = que.pop(0)
            ans.append(cur_course)
            for course in courses[cur_course]:
                pre_nums[course] -= 1
                if pre_nums[course] == 0:
                    que.append(course)

        return ans if len(ans) == numCourses else []


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findOrder(2, [[1, 0]])
    print(test1, [0, 1])
    assert test1 == [0, 1]

    test2 = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print(test2, [0, 1, 2, 3])
    assert test2 == [0, 1, 2, 3]

    test3 = sol.findOrder(1, [])
    print(test3, [0])
    assert test3 == [0]
