'''
https://leetcode.com/problems/open-the-lock/?envType=daily-question&envId=2024-04-22
'''

from collections import deque

from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dial = -1
        tried = set(deadends)
        que = deque(["0000"])

        while que:
            bfs_size = len(que)
            dial += 1
            for _ in range(bfs_size):
                cur_num = que.popleft()

                if cur_num == target:
                    return dial

                if cur_num in tried:
                    continue

                tried.add(cur_num)
                
                next_nums = []
                for idx, ch in enumerate(cur_num):
                    next_nums.append(cur_num[:idx] + str((int(ch) - 1) % 10) + cur_num[idx + 1:])
                    next_nums.append(cur_num[:idx] + str((int(ch) + 1) % 10) + cur_num[idx + 1:])

                que.extend(next_nums)

        return -1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.openLock(deadends = ["0201", "0101", "0102", "1212", "2002"], target = "0202")
    assert test1 == 6
    
    test2 = sol.openLock(deadends = ["8888"], target = "0009")
    assert test2 == 1
    
    test3 = sol.openLock(deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target = "8888")
    assert test3 == -1
    