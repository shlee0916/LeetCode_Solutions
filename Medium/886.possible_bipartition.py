'''
https://leetcode.com/problems/possible-bipartition/description/
'''

from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        groups = {}
        dis_map = {}
        for person in range(1, n + 1):
            dis_map[person] = []

        for dislike in dislikes:
            dis_map[dislike[0]].append(dislike[1])
            dis_map[dislike[1]].append(dislike[0])

        signed = set()
        for person in range(1, n + 1):
            if person in signed:
                continue

            stack = [(person, 0)]
            while stack:
                tmp_stack = []
                while stack:
                    cur_person, group = stack.pop()

                    if cur_person in groups and group != groups[cur_person]:
                        return False

                    if cur_person in signed:
                        continue

                    groups[cur_person] = group
                    signed.add(cur_person)

                    for hate in dis_map[cur_person]:
                        tmp_stack.append((hate, not group))

                stack = tmp_stack

        return True


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])
    print(test1, True)
    assert test1 == True

    test2 = sol.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]])
    print(test2, False)
    assert test2 == False

    test3 = sol.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])
    print(test3, False)
    assert test3 == False
