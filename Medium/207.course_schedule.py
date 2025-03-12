'''
https://leetcode.com/problems/course-schedule/
'''

class Solution:
    def canFinish(self, n, prerequisites):
        course = [[] for i in range(n)]
        degree = [0] * n

        for post, pre in prerequisites:
            course[pre].append(post)
            degree[post] += 1

        bfs = [num for num in range(n) if degree[num] == 0]

        for num in bfs:
            for c in course[num]:
                degree[c] -= 1
                if degree[c] == 0:
                    bfs.append(c)

        return len(bfs) == n


if __name__ == "__main__":
    sol = Solution()

    print(sol.canFinish(2, [[1, 0]]), True)
    print(sol.canFinish(2, [[1, 0], [0, 1]]), False)