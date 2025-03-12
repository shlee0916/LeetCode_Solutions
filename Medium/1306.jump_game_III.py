'''
https://leetcode.com/problems/jump-game-iii/description/
'''

from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        limit = len(arr) - 1

        stack = [(start, arr[start])]
        visit = set()
        while stack:
            cur_pos, jump = stack.pop()
            if cur_pos in visit:
                continue

            visit.add(cur_pos)

            if arr[cur_pos] == 0:
                return True

            next_pos = (cur_pos + jump, cur_pos - jump)
            if next_pos[0] <= limit:
                stack.append((next_pos[0], arr[next_pos[0]]))
            if next_pos[1] >= 0:
                stack.append((next_pos[1], arr[next_pos[1]]))

        return False
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.canReach(arr = [4, 2, 3, 0, 3, 1, 2], start = 5)
    print(test1, True)
    assert test1 == True
    
    test2 = sol.canReach(arr = [4, 2, 3, 0, 3, 1, 2], start = 0)
    print(test2, True)
    assert test2 == True
    
    test3 = sol.canReach(arr = [3, 0, 2, 1, 2], start = 2)
    print(test3, False)
    assert test3 == False
    